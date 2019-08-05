---
title:  "현실적인 재료 소모"
date:   2019-08-04 20:21:03 +0900
---

## 재료가 줄어들어야지
여태까지는 편의를 위해서 공장이 갖고 있는
'총 재료' 의 양을 생각하지 않았지만,
지금 부터는 고려해보자. 재료가 떨어지면 더 주문도 하고,
초콜릿을 만들 때 재료가 조금씩 빠져나가는 편이
좀 더 진짜 공장 다울 것 같지 않을까?


## 총 재료 양 선언하기.
`factory.py` 를 열어서 다음과 같이 작성하자.
{% highlight python %}
# 이곳은 초코 공장입니다.

# 다음은 공장의 총 재료양 입니다.
kakao = 1000
sugar = 1000
milk = 1000

# 후략 ...
{% endhighlight %}
이렇게 재료의 총량을 각각 1000 씩 `선언` 했다.

## 재료를 감소시키는 방법.
여태까지는 초코의 총 무게만 구해 보았다.
이번에는 초코를 만들 때 마다 빠져나가는 재료의 양을 표현해 보려고 한다.
먼저 재료의 양을 감소 시켜보는 연습을 해 보겠다.
Python Console 을 열어서 따라해보자.
{% highlight python %}
>>> kakao = 1000
>>> sugar = 1000
>>> milk = 1000

>>> kakao = kakao - 60 # kakao 60 감소
>>> sugar = sugar - 120 # sugar 120 감소
>>> milk = milk - 100 # milk 100 감소
{% endhighlight %}

수학시간때 배웠던 방정식의 모양과는 다르기 때문에 이상하다고 느껴질 수도 있다.
수학에서 x = x + 3 같은 건 말도 안되니까. 하지만 프로그래밍에서는 전혀 이상할 것이 없다.
그 이유를 설명하겠다.

= 연산자의 특징은 '할당'을 한다는 것 외에도 하나 더 있다. 그것은
= 연산자의 **오른쪽 식이 먼저 계산된다는 것** 이다.
즉 `kakao = kakao - 60` 중에서`kakao - 60` 이 먼저 계산되는데, 
여기서 kakao 는 1000 이므로, 따라서 1000 - 60 은 940 이 된다.

그리고 곧바로 = 연산자의 할당이 진행된다. `kakao = 940` 이 실행되는 것이다. 최종적으로,
kakao 변수에는 940 이 할당된다.

한편, `kakao = kakao - 60` 을 축약해서 쓰는 방법이 있다. 많이 사용되는 방법이므로 기억해 두자.
`kakao -= 60` 이라고 쓰며, 그 효과는 완전히 동일하다. `kakao 변수에서 60을 빼라` 라는 의미이다.

마찬가지로 +=, *=, /=, //= 등이 있다.
{: .text-center}
{: .notice--info}


## '행동' 을 저장하는 방법.
초코의 총 무게도 구해 보았고, 재료를 감소시키는 것도 해 보았다.
그런데 초코를 하나 만들 때 마다 일일이 다음과 같이 입력해야 한다면
너무 번거롭지 않을까?
{% highlight python %}
kakao -= 60
sugar -= 120
milk -= 100
{% endhighlight %}

밀크초코와 다크 초코도 작성해 보면
{% highlight python %}
kakao -= 60
sugar -= 120
milk -= 100

kakao -= 60
sugar -= 120
milk -= 200

kakao -= 90
sugar -= 120
milk -= 100
{% endhighlight %}

우리가 `sugar = 120` 을 했던 것 처럼, `kakao -= 60 sugar -= 120 milk -= 100` 도
어딘가 저장을 했다가 불러올 수 있는 방법이 있다.
아쉽게도, `choco = kakao -= 60 sugar -= 120 milk -= 100` 같은 방법은 아니다.
`함수`라고 하는 방법이다.

## 함수
프로그래밍에서 말하는 함수는 수학시간에 배운 함수와 비슷하다. 그런데 비슷하면서도
조금 다르다.
먼저 "올바르게" 작성된 함수를 보고, 차근차근 살펴보자.
{% highlight python %}
kakao = 1000
sugar = 1000
milk = 1000

# 중략

def make_choco(): # def 는 define 의 약자로, '정의'한다는 뜻이다.
    # 함수 안에는 choco 를 만드는 과정이 그대로 적혀 있다.
    kakao -= 60
    sugar -= 120
    milk -= 100

{% endhighlight %}

def 는 '함수를 정의한다' 는 뜻으로, 일반적인 변수가 아니라, `키워드` 라고 한다.
`키워드` 는 파이썬 안에서 특별한 의미를 지니는 기호이다. +, * 등의 연산자도
저마다 특별한 의미를 가졌던 것 처럼, def 도 '함수를 정의한다'는 고유의 의미를 가지고 있다.

def 다음에 곧바로 등장하는 `make_choco` 는 함수의 이름이다. 이처럼
def 다음에는 바로 그 함수의 이름이 와야 한다.

그 다음에 `()`는 함수의 '인자' 를 전달하는 부분인데, 
수학시간에 `f(x) = y` 에서 `(x)` 부분과 관련이 깊다. 다음에 더 자세히 배우자.

`:` 는 단순히 `이 다음부터 함수의 내용(body)입니다.` 라는 의미라고 생각하면 된다.

## 스코프
그런데 Pycharm 에 위 함수를 입력해 보면, 곳곳에 빨간 줄이 그어지는 것을
보게 될 것이다. 실행을 해 보면 에러도 난다.
```
Traceback (most recent call last):
  File "C:/Users/aliwo/PycharmProjects/ChocoPy/factory.py", line 19, in <module>
    make_choco() # 함수 호출
  File "C:/Users/aliwo/PycharmProjects/ChocoPy/factory.py", line 15, in make_choco
    kakao -= 60
UnboundLocalError: local variable 'kakao' referenced before assignment
```
아까 까지만 해도 잘 동작했던 kakao -= 60 가 왜 에러를 일으키는것일까?
이 책이 함수를 작성하는 방법을 잘못 알려주는 것일까? (그건 아니다.)
이는 변수의 `스코프(scope)` 때문에 발생하는 문제이다. 스코프 챕터에서 살펴보자.






