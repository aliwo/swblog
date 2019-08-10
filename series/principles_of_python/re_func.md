---
title:  "변수의 스코프"
date:   2019-08-06 10:21:03 +0900
---

## 함수와 스코프

'함수' 챕터에서 다음 문제에 봉착했었다.
{% highlight python %}
kakao = 1000
sugar = 1000
milk = 1000

# 중략

def make_choco():
    kakao -= 60 # 함수안에서 전역변수를 수정하려고 시도한다.
    sugar -= 120 # 
    milk -= 100
{% endhighlight %}

## return

모범적인 해결 방법은 다음과 같다.

{% highlight python %}
kakao = 1000
sugar = 1000
milk = 1000

# 중략

def make_choco():
    kakao -= 60 # 함수안에서 전역변수를 수정하려고 시도한다.
    sugar -= 120 # 
    milk -= 100
{% endhighlight %}


