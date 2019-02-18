---
title:  "집합"
date:   2019-02-17 20:21:03 +0900
---

## 벤 다이어 그램
중학생 시절 배웠던 수학의 벤 다이어그램을 생각해 보자.

![image-center]({{ site.baseurl }}/assets/images/2019-02-17-set.jpg){: .align-center}

집합 A 의 특징은 다음과 같다.
* 집합 요소 1, 2, 4 를 가지고 있다.
* 요소 들 간에 특별히 순서가 정해져 있지 않다. 1, 2, 4 혹은 4, 1, 2 등으로 정해진 것이 아니다.
* 중복을 허용하지 않는다. 4가 두 번 들어가거나 1이 두 번 들어가는 경우는 없다.

파이썬의 집합 자료형도 수학의 집합 처럼 순서가 정해져 있지 않고, 중복을 허용하지 않는 자료형이다.


## 집합 자료형의 생성
{% highlight python %}
>>> my_set = {1, 4, 2}
>>> my_set = set([1, 4, 2])
{% endhighlight %}

집합 자료형을 생성하기 위한 방법은 여러가지 있다.
그 중 두 가지 방법을 소개한다.
가장 간단한 방법은 중괄호 안에 원하는 요소를 집어 넣는 것이다.
이외에도 set() 의 괄호 안에 리스트를 집어 넣어서 생성할 수도 있다.


## 집합 자료형의 기능

{% highlight python %}
>>> my_set = set([1, 4, 2])
>>> my_set.add(3)
>>> my_set
{1, 2, 3, 4}
{% endhighlight %}
생성된 집합에 요소를 추가하고 싶다면 add() 를 사용한다.


{% highlight python %}
>>> my_set = set([1, 4, 2])
>>> my_set2 = {1, 2, 8}
>>> my_set.intersection(my_set2)
{1, 2}
{% endhighlight %}
두 개의 집합 간에 교집합을 구하고 싶다면 intersection() 을 사용한다.


{% highlight python %}
>>> my_set = set([1, 4, 2])
>>> my_set2 = {1, 2, 8}
>>> my_set - my_set2 
{4}
{% endhighlight %}
두 개의 집합 간에 차집합을 구하고 싶다면 그냥 빼면 된다.


{% highlight python %}
>>> my_set = set([1, 4, 2])
>>> my_set2 = {1, 2, 8}
>>> my_set.union(my_set2)
{1, 2, 4, 8}
{% endhighlight %}
단, 합집합을 구할 때에는 + 기호가 아니라 union() 을 사용한다.



## 리스트의 중복 제거
set 자료형은 **중복을 허용하지 않는다.** 라는 특성 때문에 간단하게 리스트의 중복을 제거하는 용도로 자주 사용된다.
{% highlight python %}
>>> list(set([1, 3, 2, 3, 2])) # 리스트를 set 으로 만들고, 다시 set 을 리스트로 만든다.
[1, 2, 3] # 결과: 중복이 제거된 리스트
{% endhighlight %}









