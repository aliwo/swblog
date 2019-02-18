---
title:  "정수와 실수"
date:   2019-02-13 20:21:03 +0900
---


## 두 가지 숫자 자료형
기본적으로 숫자를 표현하는 자료형은 두 개가 있다.
* 하나는 정수를 표현하는 integer (줄여서 int)
* 다른 하나는 실수를 표현하는 float (줄여도 float)


## float
소수점 . 이 붙어있는 숫자라면 무조건 float 으로 취급된다.
1.0, 3.0 등 실제로는 정수인 숫자도 소수점이 붙어있기
때문에 모두 실수(float) 로 취급 된다.

{% highlight python %}
>>> type(3.0)
<class 'float'>

>>> type(8.5)
<class 'float'>
{% endhighlight %}






