---
layout: single
title:  "kubernetes -> kubectl port-forward -> docker -> local 통로 만들기"
date:   2020-08-17 11:10:03 +0900
categories: [kubernetes, elasticsearch, kibana]
---

## 쿠버네티스 클러스터 에서 돌아가는 kibana 에 접근하는 쉬운 방법이 없을까?
* kibana 서비스를 loadbalancer 에 붙여서 외부에 공개하는 방법
* port-forward 를 사용하는 방법
둘 다 장단점이 있다. 외부에 공개해버리면 보안성은 떨어지지만 언제든 핸드폰이나
패드로 kibana 에 접근 할 수 있다. 한 편 `port-forward`를 사용하면 `port-forward` 가 항상
컴퓨터에서 돌아가야 하고, `kubectl port-forward` 를 할 수 없는 기기에서는 kibana에 접근할 수 없다.
그래도 보안 측면에서는 더 안전하다.

## 그래서 생각한 방법
처음에 세팅할 때는 어마어마하게 불편한 데, 한 번 설정해 놓으면 너무나 편한 방법이라고 하겠다. 지금까지도 잘 쓰고 있다.
1. ubuntu image 준비
2. gcloud, kubectl 세팅. gke 연결
3. 이미지 커밋
4. kubectl port-forward 를 실행하도록 `docker run`
5. docker 가 항상 돌아가고 있으므로 localhost:5601 로 접근하면 언제든지 kibana 접속!

## 명령어
세팅하는 방법(1에서 4까지)은 생략 ^^
아래 명령어는 kibana 는 아니고 elastic search 를 port-forward 한다.
```
docker run --restart unless-stopped --name elastic_forward -p 9200:9200 playground1 kubectl port-forward svc/quickstart-es-default --address 0.0.0.0 -n sy-elastic 9200:9200
```

