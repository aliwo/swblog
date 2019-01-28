---
title:  "코드 블록"
date:   2019-01-17 20:21:03 +0900
---

## 코드 블록
코드블록은 한 문단의 코드이다.
문장이 모여 문단이 되고 문단이 모여 글이 되듯이
파이썬 코드가 모여 코드 블록을 형성하고,
파이썬 코드 블록들이 모여 하나의 파이썬 프로그램을 이룬다. 


## 코드 블록작성

기본적으로, 한 line 당 한 문장을 작성하고, 개행한다.

{% highlight python %}
my_variable = 3
print(my_variable) 
{% endhighlight %}

한 Line 에 여러 문장을 작성하고 싶다면 방법은 있다. ;(세미콜론)을 사용하면 된다. 그러나 권장되는 방법은 아니다.

{% highlight python %}
my_variable = 3; print(my_variable) # 출력: 3 
{% endhighlight %}


## 코드블록의 구분
파이썬은 코드블록을 표현하기 위해 들여쓰기를 사용합니다.
이 들여쓰기는 들여쓰기 한 번 당 스페이스 바 4번 입니다.
Pycharm 등의 개발도구는 자동으로 tab 을 스페이스바 4개로 바꿔주므로
여러분은 편하게 tab 을 사용하셔도 좋습니다.

{% highlight python %}
class MyClass:
    my_variable = 3 # 스페이스 바 4 개로 들여씀
    my_second_variable = 4
{% endhighlight %}
