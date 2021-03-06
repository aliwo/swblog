---
title:  "정수와 실수"
date:   2019-07-16 20:21:03 +0900
---

## 나눗셈의 결과
mild_choco 를 만들 때 / 를 쓰느냐, // 를 쓰느냐에 따라서 출력값이 '살짝' 달랐다.
{% highlight python %}
>>> sugar = 120
>>> milk = 100
>>> mild_choco = 60 / 2 + sugar + milk 
>>> mild_choco
250.0
>>> mild_choco2 = 60 // 2 + sugar + milk
>>> mild_choco2 
250
{% endhighlight %}


## 왜 .0 이 붙을까?
그렇다면 왜 mild_choco 에만 .0 이 붙을까?

파이썬에서 기본적으로 숫자를 표현하는 자료형은 두 개가 있다.
* 하나는 정수를 표현하는 integer (줄여서 int)
* 다른 하나는 실수를 표현하는 float (줄여도 float)

연산자 '/' 을 사용하면 그 결과는 무조건 float 이 되며, 연산자 '//' 을 사용하면
나눗셈의 나머지를 버린채, 그 결과는 무조건 int 가 된다.

여러분은 나머지를 생각할 필요가 없는 상황에서 `//` 를 사용하면 된다.


## 자료형이란?
앞서 '자료형' 이란 단어가 나왔다. 영어로는 Type 이라고 하는데, 그 뜻 그대로
데이터의 '종류' 를 말한다. 정수라면 integer 타입, 실수라면 float 타입,
그 의외에도 리스트라면 list 타입, 문자열(우리가 흔히 이야기 하는 '글씨')이라면 string
타입과, 다른 여러가지 타입 등이 있다.


## 250.0 과 250 은 같을까?
다른 프로그래밍 언어를 배워봤다면 파이썬이
250.0 과 250 을 '같다' 라고 말하는 점에서 놀라겠지만, 파이썬에선 그렇다.
2개의 변수를 비교할 때에는 == 연산자를 사용한다. (=은 '할당' 에 사용되기 때문에 == 이다.)
한 번 비교해보자.

{% highlight python %}
>>> mild_choco == mild_choco2 # 250.0 과 250 이 같을까요?
>>> True # 네 같아요!
{% endhighlight %}

mild_choco 와 mild_choco2 는 그 값이 같다.


## 실수로 취급되는 기준
소수점 . 이 붙어있는 숫자라면 무조건 float 으로 취급된다.
1.0, 3.0 등 실제로는 정수인 숫자도 소수점이 붙어있기
때문에 모두 실수(float) 로 취급 된다.

아직은 type() 이 무엇을 의미하는지 모르겠지만, type() 의
괄호 안에 값을 집어 넣으면, 무슨 타입인지 알려준다.
한 번 해보자.

{% highlight python %}
>>> type(3.0)
<class 'float'>

>>> type(8.5)
<class 'float'>

>>> type(3)
<class 'int'>
{% endhighlight %}

이렇 듯, 점(.) 이 붙어있는 숫자는 모두 float 이다.


## 실수를 정수로, 정수를 실수로
실수를 정수로 바꾸려면 다음과 같이 한다.

{% highlight python %}
>>> int(3.0)
3
>>> int(3.9)
3
{% endhighlight %}
int() 안에 어떤 실수를 넣으면, 소수점 밑의 숫자는 버리고 
정수 값을 결과로 얻을 수 있다.

반대로 정수를 실수로 바꾸는 것도 가능하다.
{% highlight python %}
>>> float(3)
3.0
{% endhighlight %}




