---
title:  "산술 연산자"
date:   2019-01-26 20:21:03 +0900
---

## 파이썬 계산기
간단한 숫자 계산에서부터 복잡한 수학식 까지 파이썬으로 전부 계산할 수 있다.
파이썬 콘솔을 열어서 다음을 입력해보자.
{% highlight python %}
>>> 1 + 1
2

>>> 10 - 1
9

>>> 10 / 5
2.0

>>> 2 * 4
8
{% endhighlight %}

특정 연산을 의미하는 기호를 연산자라고 한다.
예를 들어 수학에서 + 가 더하기를 의미한다는 것은 누구나 알고 있을 것이다.
마찬가지로 프로그래밍에서도 + 는 더하기를 의미하는 기호이며, 더하기라는 연산을 의미하기 때문에 연산자이다.
+, -, *, / 등 숫자를 계산하는 연산자를 산술 연산자라고 한다.

파이썬은 가감승제 말고도 몇 가지 산술 연산자를 더 지원한다.
{% highlight python %}

>>> 10 // 3 # 정수 나눗셈 연산자. 소수점 값을 전부 버린다.
3

>>> -4 // 3 # 음수의 경우에는 내림 처리한다.
-2

>>> 10 % 3 # 나머지 연산자. 나눗셈의 나머지를 구한다.
1

>>> 2 ** 3 # 제곱 연산자.
8

{% endhighlight %}


## = 을 같이 사용하기

산술 연산자와 할당 연산자를 조합해서 사용할 수도 있다.

{% highlight python %}

>>> my_number = 2

>>> my_number += 3 # my_number = my_number + 3 과 같다. 

>>> my_number
5

{% endhighlight %}


## ++ 와 \-\-
혹시 자바에서 봤던 ++ 혹은 \-\- 를 찾고 있는가? 파이썬에서는 없다. 잠시 잊어버리자.



## 소괄호 사용하기
간단한 문제를 내겠다.

3 + 4 * 2 = ?
{: .text-center}


맞췄는가? 답은 당연히 11이다. 14가 나온 사람은 없을 거라 믿겠다.
이제 파이썬에서 위 식을 입력해 계산해 보자.
{% highlight python %}
>>> 3 + 4 * 2
11
{% endhighlight %}
파이썬도 계산 결과로 11을 돌려준다.


답을 14가 나오도록 바꾸려면 어떻게 할까? 더 읽어나가기 전에 스스로 한 번 해보길 바란다.
여러분은 이미 어떻게 해야 할지를 알고 있다.

<br><br>

{% highlight python %}
>>> (3 + 4) * 2 
14
{% endhighlight %}
답은 소괄호를 사용하는 것이다. 
수학 시간때 소괄호를 사용하던 것 처럼, 파이썬에서도 소괄호를 사용해서
연산의 우선순위를 제어할 수 있다.


## 연습문제
이차 방정식 ax**2 + bx + c 의 a b c 가 주어졌을 때, x 를 구하는 프로그램을 작성해보자.
근의 공식은 인터넷 검색하면 금방 나온다.









