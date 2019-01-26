---
title:  "코드 블록"
date:   2019-01-17 20:21:03 +0900
---

<h2>코드 블록</h2>
코드블록은 한 문단의 코드이다.
문장이 모여 문단이 되고 문단이 모여 글이 되듯이
파이썬 코드가 모여 코드 블록을 형성하고,
파이썬 코드 블록들이 모여 하나의 파이썬 프로그램을 이룬다. 


<h2>코드 블록작성</h2>

기본적으로, 한 line 당 한 문장을 작성하고, 개행한다.

{% highlight python %}
my_variable = 3
print(my_variable) 
{% endhighlight %}

한 Line 에 여러 문장을 작성하고 싶다면 방법은 있다. ;(세미콜론)을 사용하면 된다. 그러나 권장되는 방법은 아니다.

{% highlight python %}
my_variable = 3; print(my_variable) # 출력: 3 
{% endhighlight %}


파이썬은 함수 블록 혹은 클래스 블록을 표현하기 위해 {}'중괄호' 를 사용하지 않습니다. 대신 tab (혹은 space bar 4번)을 사용해서 들여씁니다.

{% highlight python %}
class MyClass:
    my_variable = 3
    my_second_variable = 4
{% endhighlight %}
