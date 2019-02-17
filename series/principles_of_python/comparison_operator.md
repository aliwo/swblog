---
title:  "비교 연산자"
date:   2019-02-17 20:21:03 +0900
---

## 크고 작음을 분별하는 연산자
파이썬 콘솔을 열고 다음을 입력해보자.
{% highlight python %}
>>> 3 > 1
True
{% endhighlight %}

< 와 > 는 크고 작음을 비교한다. 3 > 1 에서 실제로 3은 1보다 크므로, 그 결과는 True 가 된다.


{% highlight python %}
a = 3
b = 1

if a > b:
    print('a 가 큽니다.')
else:
    print('b가 큽니다.')
{% endhighlight %}


<, > 연산자들은 초과와 미만 여부를 검사하고
<= , >= 연산자들은 이상, 이하 여부를 검사한다.






