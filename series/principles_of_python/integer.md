---
title:  "정수와 실수"
date:   2019-02-13 20:21:03 +0900
---


## 두 가지 숫자 자료형
기본적으로 숫자를 표현하는 자료형은 두 개가 있다.
* 하나는 정수를 표현하는 integer (줄여서 int)
* 다른 하나는 실수를 표현하는 float (줄여도 float)


## 실수로 취급되는 기준
소수점 . 이 붙어있는 숫자라면 무조건 float 으로 취급된다.
1.0, 3.0 등 실제로는 정수인 숫자도 소수점이 붙어있기
때문에 모두 실수(float) 로 취급 된다.

{% highlight python %}
>>> type(3.0)
<class 'float'>

>>> type(8.5)
<class 'float'>
{% endhighlight %}

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

## 반올림

반올림을 하고 싶다면 round() 함수를 사용한다.
{% highlight python %}
>>> round(3.4)
3
>>> round(3.9)
4
{% endhighlight %}



## 올림, 내림
int() 는 소수점 밑의 숫자를 버리는 방식으로 실수를 정수로 바꾸었다.
round() 를 사용하면 반올림도 할 수 있었다.
그런데 올림, 내림을 하고 싶을 때는 어떻게 할까?

이 때는 파이썬의 math 모듈의 도움을 받아야 한다.
모듈이란 여러가지 도움이 되는 기능들을 종류별로 한 데 모은 것을 의미한다.
(모듈의 자세한 구조에 대한 내용은 '모듈' 챕터에서 배우도록 하자.)
math 모듈은 그 이름대로 수학에 관련한 기능들을 한 데 모아 놓은 모듈이다.

모듈을 사용하기 위해서는 먼저 모듈을 가져와야 하는데, `import` 키워드를 사용하면
간단하게 가져올 수 있다.


{% highlight python %}
>>> import math
{% endhighlight %}
이게 다다. import math 만으로 math 모듈을 가져올 수 있다.

나머지는 가져온 math 모듈을 사용하는 것 뿐이다.

먼저 반올림을 하려면 math.ceil() 를 사용한다. ceil 가 영어로 올림을 의미한다.

여기서 math 다음에 . (구두점) 을 붙이는 것은 

"math의 기능에 접근하겠다." 
{: .text-center}

라는 뜻이다.
따라서 math.ceil() 는 "math 의 기능 중 ceil() 을 사용하겠다" 라는 뜻이다.
그럼 이제 따라해 보자.

{% highlight python %}
>>> import math
>>> math.ceil(3.6)
4
>>> math.ceil(3.1)
4
{% endhighlight %}

잘 올림 된 것 같다.

반대로 내림을 하기 위해서는 math.floor() 를 사용한다.

{% highlight python %}
>>> math.floor(3.6)
3
>>> math.floor(3.1)
3
{% endhighlight %}

## 연습 문제

주어진 가격에 10 % 할인을 적용하는 프로그램을 작성해 보자.
마트에서 8원, 6원 등 10원보다 작은 단위를 받을 수는 없으므로
10의 자리의 수 까지 올림 해보자.
예를 들어
12880원을 10% 할인 하면 11600원 이므로 12880 을 입력했다면 결과로 11600 이 화면에 출력되어야 한다.
{% highlight python %}
price = input()
# 나머지를 작성해 보자!
{% endhighlight %}

**힌트:** math.ceil() 을 사용하자! 
{: .notice--info}





