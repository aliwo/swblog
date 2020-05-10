---
layout: single
title:  "vim 명령어 모음"
date:   2020-04-07 11:10:03 +0900
categories: [vim]
---


해괴한 vim 없이 여태껏 잘 살 수 있었지만… 
Kubernetes 시험 때문에 공부해 봅니다. ^^


## 저장, 종료
Normal 모드에서 : 콜론을 입력하는 것으로 command 모드로 접근한다.

```
:w 저장, write
:q 나가기, quit
:wq save and exit
:q! save without exit
```

## line number

```
:set number 라인 넘버를 보여준다.
```


## 입력
```
:i 입력모드
```
esc 를 누르면 입력모드에서 빠져 나간다.

## 복붙
normal 모드에서
```
yy 라인 복사
p 붙여넣기
```


## 삭제
normal 모드에서...
```
dd 한 줄 삭제 (콜론 없이 dd만 입력... 황당하네)
```

## 실행취소
normal 모드에서
```
u 는 undo 
ctrl + r 는 redo
```

## 찾기
normal 모드에서
```
/검색어
?검색어
```
/는 맨 위에서 부터, ? 는 맨 아래에서 부터 탐색한다.


## 찾고 바꿔치기
```
:%s/검색어/바꿀 문자열/g
```
끝의 g 는 greedy 를 의미하는 듯 (모든 occurrence 를 찾는다.)
gc 를 입력하면 파일 안의 모든 검색어를 일일이 순회하면서 바꿀지 말지를 물어본다.


## autoindent
:set autoindent
:set expandtab 

expandtab 은 tab 을 space 로 바꿔준다.