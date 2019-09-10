---
title:  "DateTime"
date:   2019-09-09 11:21:03 +0900
---

![image-center]({{ site.baseurl }}/assets/images/2019-09-09-choco2.jpg){: .align-center

## 날짜와 시간을 다루는 방법
초콜릿 하면 떠오르는 것 중에서 '제조일자'와 '유통기한' 도 있었다.
그렇다면 파이썬 프로그램에서 날짜와 시간을 표현하려면 어떻게 해야 할까?

## datetime 모듈
파이썬 콘솔을 열어서 따라해보자.

{% highlight python %}
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 9, 9, 15, 22, 19, 941214)
{% endhighlight %}

`datetime.now()` 를 입력한 순간 반환되는 것은 현재 시각을 담고 있는
datetime 객체이다. 

{% highlight python %}
type(datetime.now())
<class 'datetime.datetime'>
{% endhighlight %}

## datetime 활용하기



