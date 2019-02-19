---
title:  "Lambda"
date:   2019-02-19 09:21:03 +0900
---

## 멕가이버 칼

우리에겐 멕가이버 칼로 친숙한 swiss army knife는 칼 자루 하나에
칼, 드라이버, 손톱깎이등 다양한 도구가 합체되어 있다.

멕가이버 칼처럼 도구 이면서 다른 여러가지 도구를 포함하고 있는 도구를
파이썬으로 표현해 보겠다.

{% highlight python %}

def swiss_army_knife(target):
    def knife():
        print('자릅니다.')

    def nail_clipper():
        print('손톱을 깎습니다.')

    def opener():
        print('병을 땁니다.')

    if target == 'knife':
        return knife

    if target == 'nail_clipper':
        return nail_clipper

    if target == 'opener':
        return opener

        
{% endhighlight %}


## nested function

함수 swiss_army_knife() 는 함수이면서
자신 안에서 또 다른 함수를 정의했다.



함수도 변수처럼 리턴할 수 있다.
또한 리턴된 함수를 변수에 할당해 호출하는 것도 가능하다.


{% highlight python %}
my_gadget = swiss_army_knife('knife')
my_gadget() # 자릅니다. 출력
{% endhighlight %}



## 람다
람다는 간단한 익명함수를 작성하는데에 쓰입니다.

lambda <인자> : 문장


















