---
layout: single
title:  "statefulset 으로 실행되는 mysql 의 timezone 변경"
date:   2020-06-21 11:10:03 +0900
categories: [kubernetes, mysql]
---


## 환경
* GKE
* Mysql (StatefulSet 으로 배포)
* bitnami mysql8 이미지 사용


## 개요

갓 서비스를 시작한 스타트업은 쿠버네티스를 써야 할 이유가 없다. 오토스케일링이나, 오토힐링이 필요한 만큼의
부하가 들어오질 않기 때문이다. AWS 를 쓸 때에도 가장 사양 낮은 인스턴스를 써도 자원이 남아돌 때가 더 많다.

그런데 난 쿠버네티스를 썼다. 왜? 공부하려고 ㅎㅎ... 아무래도 비용이 가장 부담되니까 managed 데이터베이스를 못 쓰고
statefulset 으로 mysql 을 돌리는 형국이다.

현재 helm3 를 사용해서 <a href="https://hub.helm.sh/charts/bitnami/mysql" target="_blank">mysql 8</a> 을 설치해 놓고
쓰고 있다.

## TimeZone 바꾸기

그런데 이 mysql 의 timezone 을 바꾸려면 어떻게 해야 할까?
공식 문서에서 마땅한 가이드를 못 찾아서 좀 해맸는데, 방법은 간단하다.

![image-center]({{ site.baseurl }}/assets/images/2020-07-02-mysql.jpg){: .align-center}

config map 중에 <헬름 릴리즈 명>-mysql-master 로 되어있는 config map 이 있다. 이게 mysql 설정 파일이다.
여기서
```
[mysqld]
...기존 설정
default-time-zone = '+9:00'
```
끝에 default-time-zone 을 추가해주면 된다. 대한민국은 UTC + 9 이니까 +9:00으로 설정한다.
설정후에 실행중인 pod 를 죽인다.
현재 실행중인 mysql pod 을 죽이면 새 pod 가 실행되고, timezone 값이 바뀐 것을 확인할 수 있다.
mysql 에서 확인하려면...
```mysql
SELECT NOW();
```




