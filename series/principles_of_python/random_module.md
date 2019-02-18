---
title:  "랜덤 모듈"
date:   2019-02-17 09:21:03 +0900
---




## 가끔 나오는 맛 없는 버거
가끔은 맛 없는 버거가 나오도록 바꾸고 싶다. taste 값이 랜덤 하게 정해지도록 하는 것이다.
랜덤한 값이 나오도록 하기 위해서, 파이썬의 random 라이브러리를 사용해 보도록 하겠다.

{% highlight python %}
class Burger:
    ingredients = ['bun', 'patty', 'lettuce', 'tomato', 'pickle']
    taste = 5 # 5 out of 5

    def __init__(self, pickle):
        if pickle is False: # pickle 은 True or False 값이다.
            self.ingredients.remove('pickle')

{% endhighlight %}














