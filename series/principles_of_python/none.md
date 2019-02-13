---
title:  "None 자료형"
date:   2019-01-24 09:21:03 +0900
---

## 비어있는 상자
앞서 변수에 대해 이야기할 때 변수를 상자에 빗대에서 설명한 적이 있다.
상자 안에 숫자, 문자열 등의 다양한 값을 넣을 수 있고, 그 값을 꺼내서 쓸 수 있다고 했다.
그렇다면 아직 아무것도 넣기 전의, 비어있는 상자도 존재할 수 있을까?


## None
있다. '비어있음' 을 표현하는 키워드가 바로 None 이다.
{% highlight python %}
>>> my_variable = None
>>> my_variable

{% endhighlight %}
아무것도 출력되지 않는다. 인터프리터 모드에서 None 변수의 이름을 대면
그냥 공백이 출력된다.

{% highlight python %}
>>> print(my_variable)
{% endhighlight %}
print 함수는 my_variable 이 None 타입 이라는 것을 알려준다.

## None 의 특성
None 은 if 문에서는 '거짓' 으로 인식된다.
{% highlight python %}
if None:
    print('있다')
else:
    print('None 이다.')
{% endhighlight %}


