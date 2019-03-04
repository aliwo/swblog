---
title:  "정규 표현식 시작하기"
date:   2019-03-03 16:21:03 +0900
---

## 정규표현식의 필요성

웹 프로그래밍을 하게 되면 python 프로그램 안에서 html 문자열을 다뤄야 할 일들이 종종 생긴다.

{% highlight python %}
html = '<div> <span style="background-color:blue">hello html</span> </div>'
print(html)
{% endhighlight %}

그리고 단일 html 요소의 attribute 값, (class 혹은 style 등등) 만 뽑아내야할 일들도 생긴다.
BeautifulSoup 를 사용하면 간편하게 해결할 수 있지만, 여기서는 BeautifulSoup 는 생각하지 않겠다.
파이썬의 문자열 연산만을 사용해서 span 의 style 값만 가져오는 방법을 생각해 보자.

어떤가? 딱 보아도 간단하게 끝날 것 같이 보이지는 않는다.
이러한 상황에서 정규표현식을 사용하면 얼마나 간편해 지는지 확인해 보자.  


## 정규표현식의 강력함








## 유용한 정규표현식 테스트 사이트
<a href="https://regexr.com/" target="_blank">regexr</a>













