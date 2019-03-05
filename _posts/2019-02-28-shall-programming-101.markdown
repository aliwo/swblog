---
layout: single
title:  "Bash Shell Programming 기초"
date:   2019-02-28 16:10:03 +0900
categories: [ubuntu, linux]
--- 

## 개요
리눅스를 만지작 거리다 보면 언젠가 반드시 필요한 날이 오는
Shell Programming. 그 기초부터 정리해 보도록 하겠다.


## Bash 랑 Shell 이랑 같은 거에요?
결론부터 말하자면, 아니다.
아닌데, 혼용해서 쓰는 경우가 많다.
<a href="https://askubuntu.com/questions/172481/is-bash-scripting-the-same-as-shell-scripting" target="_blank"> 링크
 </a>



## Hello World
다음 코드는 단순히 문자열을 출력한다.
printf 는 C 언어의 `printf` 처럼 문자열 포맷팅을 이용할 수 있다.
```bash
echo "hello world"
printf "hello world"
printf "%s %s" hello world
```

## 주석
\# 으로 시작하면 주석이다.


## shebang(셔뱅) line
(shebang, 영어로 읽으면 어감이 좋지 않다.)
파일의 맨 첫번째 줄에 #! 으로 시작하는 부분을 shebang 이라고 한다.
해당 스크립트를 실행할 실행기의 경로를 적어주는 것이 목적인데,
셸 스크립트의 경우 `#!/usr/bin/env bash` 가 보통의 예다. 


## 변수 할당과 호출
앞 뒤로 공백없이 `=`을 사용하면 변수 할당이다.
```bash
#!/usr/bin/env bash
string="hello world"
echo $string
```
변수를 호출할 때에는 $ 표시를 변수 이름 앞에 붙인다. (php랑 닮았다.)


## 예약 변수

* HOME : 사용자의 홈 디렉토리
* PATH : 실행 파일을 찾을 경로
* USER : 사용자의 이름
* PWD : 스크립트를 실행하는 현재 디렉터리. 주의! 스크립트 가 위치한 디렉터리가 아님!

## 매개변수

* $0 : 실행된 스크립트 이름
* $1 : 스크립트에 첫번째로 전달된 인자. 순서대로 $1, $2 ...


## 특수 매개변수

* $$ : 현재 스크립트의 PID
* $? 최근에 실행한 명령어, 함수 등의 종료 상태가 담긴 변수

## 환경변수
export 키워드를 사용해서 변수를 할당하면 환경변수를 설정한다.
환경 변수는 다른 스크립트에서도 쓸 수 있다.
```bash
#!/usr/bin/env bash
export my_var="hello"
echo $my_var
```


## 쌍 따옴표

쌍 따옴표로 문자를 둘러치면 "이건 문자열 이에요" 라는 뜻이다.

```bash
echo "this is my text"
```

대신 ``$, `, \ `` 등의 문자열은 "" 안에서도 그 특별한 효과를 유지한다.



## Boolean
참, 혹은 거짓을 구분하려면 다음 예제를 먼저 보자.

```bash
#!/usr/bin/env bash
my_var1="hello"
my_var2="world"
my_var3="hello"

[ $my_var1 == $my_var3 ] ;
result=$?

echo $result
```
처음보는게 나왔다. [] (bracket 이라고 부른다.) 는 무엇을 의미할까?
<a href="https://stackoverflow.com/questions/11796751/what-does-do-in-bash" target="_blank">링크</a>

'[', 즉 여는 중괄호는 리눅스의 /user/bin/test 를 의미한다. 

\[(여는 중괄호) 부터 \](닫는 중괄호)까지를 test 를 사용해서 실행한 뒤,
그 결과를 $? 로 가져오는 것이다.


## 조건문



## $(명령)

`$(명령)`은 해당 명령을 실행하고, `$(명령)`의 결과값으로 그 자리를 대신하라는 뜻이다.
예를 들어 
```bash
echo "today is $(date)"
```
를 하면
 
```
today is ... Thu Feb 28 23:47:07 KST 2019
``` 

이런 결과가 나온다.
<a href="https://stackoverflow.com/questions/27472540/difference-between-and-in-bash" target="_blank">
스택 오버플로</a>



## TODO: 연습문제?



## 참고

<a href="https://blog.gaerae.com/2015/01/bash-hello-world.html" target="_blank">
 잘 정리되어 있는 링크  </a>

``











