---
layout: single
title:  "ssl, jdbc를 사용하는 logstash를 kubernetes에 배포하기"
date:   2020-08-09 11:10:03 +0900
categories: [kubernetes, logstash]
---

## ECK에서 Logstash는 지원이 안된다고?? 
현재 ECK에서 logstash를 지원하지 않는다. 짱 불편하다. 하지만 뭐 어쩌겠나.
순정 docker 이미지를 써서 배포해 보겠다.


## 해 볼 것
이번에 배포할 logstash 는 다음과 같은 기능을 갖는다.
1. jdbc input 을 사용해서 mysql로부터 input을 받아들인다.
1-1. 이를 위해 pod lifecycle 을 사용해서 jdbc driver 를 다운로드 받는다.
1-2. configMap을 volume 으로 마운트해 설정 파일로 활용한다.
2. ECK 에서 지원하는 SSL과 인증서를 사용해 elasticsearch 와의 보안 연결


## 순서
1. configmap (pipeline) 준비
2. deployment 준비
3. 배포

## ConfigMap 준비하기

pod 가 시작하자마자 jdbc 드라이버를 다운로드 받는 스크립트를 준비한다.
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: logstash-start
  namespace: <원하는 네임스페이스>
data:
  start.sh: |
    #!/bin/bash
    curl -L -O https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.18.tar.gz
    tar -xvf ./mysql-connector-java-8.0.18.tar.gz
    mv ./mysql-connector-java-8.0.18/mysql-connector-java-8.0.18.jar ./lib/mysql-connector-java-8.0.18.jar
```
쉬뱅 (`#!/bin/bash`) 을 안 붙이면 권한 에러가 나더라. `|` 도 붙여야 멀티 라인으로 인식되니까 빼먹지 않도록 하자.



## PipeLine
이것도 configMap 으로 저장해 둔다.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: logstash-user-pipeline
  namespace: sy-elastic
data:
  user-pipeline.conf: |
    input {
        jdbc {
            jdbc_driver_library => "/usr/share/logstash/lib/mysql-connector-java-8.0.18.jar"
            jdbc_driver_class => "com.mysql.jdbc.Driver"
            jdbc_connection_string => "jdbc:mysql://mysql pod의 서비스 혹은 ip/production"
            jdbc_user => "root"
            jdbc_password => "데이터베이스 비밀번호"
            jdbc_paging_enabled => true
            tracking_column => "unix_ts_in_secs"
            use_column_value => true
            tracking_column_type => "numeric"
            schedule => "* * * * *" # Query주기 설정
            statement => "쿼리문"
        }
    }

    filter {
        mutate {
            copy => {
                "id" => "[@metadata][_id]"
                "unix_ts_in_secs" => "[@metadata][unix_ts_in_secs]"
            }
            remove_field => ["id", "@version", "unix_ts_in_secs"]
        }
    }

    output {
         elasticsearch {
             ssl => true
             cacert => "마운트한 ssl 인증서 파일의 위치"
             user => elastic
             password => 패스워드
             hosts => ["https://엘라스틱서치 서비스:9200"]
             index => "sy-users"
             document_id => "%{[@metadata][_id]}"
         }
        stdout {
            codec => "rubydebug"
        }
    }
```

ssl을 사용하는 elasticsearch에 연결하려면 `ssl => true` 와 `cacert => "마운트한 ssl 인증서 파일의 위치"` 가 필요하다.



## Deployment

이미지는 logstash:7.8.0 을 사용한다. 이미 jdbc input 이 설치되어 있으므로
jdbc driver 만 다운로드 받아 사용하면 된다. 플러그인 설치는 필요 없다.
```yaml
      - image: logstash:7.8.0
```

jdbc driver 를 다운로드 받는 명령어를 /start/start.sh 경로에 담을 것이다.
이를 pod 시작 직후에 실행한다.
```yaml
        lifecycle:
          postStart:
            exec:
              command:
                - /start/start.sh
```

Volume 3 개를 mount 한다. pipeline 설정, ssl 인증서, start/sh 스크립트.
```yaml
      volumes:
        - configMap:
            name: logstash-user-pipeline
          name: logstash-user-pipeline
        - name: es-certs
          secret:
            defaultMode: 420
            secretName: quickstart-es-http-certs-public
        - name: start
          configMap:
            name: logstash-start
            defaultMode: 0777
```


전체 yaml 은 다음과 같다.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  creationTimestamp: null
  labels:
    app: logstash
  name: logstash
  namespace: <원하는 네임스페이스>
spec:
  replicas: 1
  selector:
    matchLabels:
      app: logstash
  strategy: {}
  template:
    metadata:
      creationTimestamp: null
      labels:
        app: logstash
    spec:
      containers:
      - image: logstash:7.8.0
        lifecycle:
          postStart:
            exec:
              command:
                - /start/start.sh
        name: logstash
        resources: {}
        volumeMounts:
          - mountPath: /usr/share/logstash/pipeline/user-pipeline.conf
            name: logstash-user-pipeline
            readOnly: true
            subPath: user-pipeline.conf
          - mountPath: /mnt/elastic/tls.crt
            name: es-certs
            readOnly: true
            subPath: tls.crt
          - mountPath: /start
            name: start
      volumes:
        - configMap:
            name: logstash-user-pipeline
          name: logstash-user-pipeline
        - name: es-certs
          secret:
            defaultMode: 420
            secretName: quickstart-es-http-certs-public
        - name: start
          configMap:
            name: logstash-start
            defaultMode: 0777
status: {}
```

## 배포
전부 `kubectl apply -f` 로 배포하면 된다.


