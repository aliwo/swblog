---
layout: single
title:  "CKA 공부... 은근 쓸모 있었던 리눅스 커맨드 모음"
date:   2020-04-20 11:10:03 +0900
categories: [linux]
---


## 프로세스

kube-apiserver 서비스 를 실행할 때 어떤 옵션이 사용되었는지 쭉 보고 싶을 때
```
ps aux | grep kube-apiserver
```

## 단축키
명령어 입력할때...
`Alt + B` (Backward) 를 하면 한 단어 뒤로, `Alt + F` (Forward) 
를 하면 한 단어 앞으로 이동한다. 맨날 화살표 연타로 이동하다가 단축키 쓰니까
너무 편한 것. kubectl get 에서 kubectl describe 로 바꿔야 할 때 느므 편함.


## count
행 수 세기
```
wc -l
```
~ 네임스페이스에는 ~ 리소스가 몇 개 있습니까? 에 대답할 때 눈으로 세는 것 보다 편하다!