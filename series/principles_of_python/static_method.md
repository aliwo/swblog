---
title:  "static method 와 class method"
date:   2019-02-17 20:21:03 +0900
---


파이썬에서 static메소드 와 class 메소드는 다음과 같이 만든다.

{% highlight python %}
class MyClass:

    @classmethod
    def my_class_method(cls, a):
        print(a)

    @staticmethod
    def my_static_method(b):
        print(b)

{% endhighlight %}

class 메소드와 static 메소드의 차이점은, class method 는 그 첫번째 인자로
cls (self 가 아님) 가 들어간다는 것이다. 이 cls 에는 해당 클래스가 들어간다.
(파이썬에서는 클래스도 객체이므로 함수의 인자로 넘겨줄 수 있다.) 














