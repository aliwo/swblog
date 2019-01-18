---
title:  "The Zen of Python"
date:   2019-01-17 20:21:03 +0900
---

<h2>import this</h2>
pycharm 을 켜자. 하단의 Python Console을 클릭하고 다음 문장을 기입하자. 그리고 엔터를 입력한다.
(\>\>\> 은 여러분이 입력할 필요 없다.)
{% highlight python %}
>>> import this
{% endhighlight %}

그럼 아래의 문구가 보인다.

``` markdown
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

갑작스러운 영어에 현기증이 난다는 독자들을 위해 한글 문서도 준비했다.<a target="_blank" 
href="https://bitbucket.org/sk8erchoi/peps-korean/src/767c779c164856af198a9d08d906a55b24652728/pep-0020.txt?at=default&fileviewer=file-view-default">
링크
</a> 천천히 읽어보자. 다 한 번쯤 읽어볼 가치가 있는 뼈가되고 살이 되는 문구라고 생각한다.

Zen of Python 을 정독했다면 이어서 아래를 읽기 바란다.

<h2>가르침</h2>
다 중요한 내용이고, 앞으로 몇 번 더 Zen of Python 의 특정 부분을 인용할 것이다. 이번에는
**There should be one-- and preferably only one --obvious way to do it.**
에 대해서 이야기 하고 싶다. 파이썬은 어떤 문제를 해결하기 위해 '가장 이상적인' 해답 하나가 존재한다고 생각한다.
그리고 그 방법은 파이썬 커뮤니티에 의해 만들어진 형용사 pythonic 에 의해 대표된다. 이 단어는 '파이썬 다운' 해결 방법을
의미하는 단어이다.

같은 문제를 놓고도 언어마다 해결하는 방식은 다르다. 예를 들어 객체지향 프로그래밍의 유명한 '다이아몬드 문제'의 경우 자바가 다중 상속을 허용하지 않고
Interface를 다중 구현 하는 방식으로 문제를 해결했다면 파이썬은 다중 상속을 허용하면서 \_\_super\_\_ 라는 키워드
를 통해 문제를 해결하는 방법을 사용했다.

pythonic 한 방식이 가장 옳은 방식이라는 억지를 부리려는 것은 아니다. 자바 개발자가 파이썬을 배우고 나서
문제를 그대로 자바식으로 해결하려고 해도 문제는 해결 될 것이다. 하지만 필자는 여러분이 이 책을 읽고 나서
파이썬은 파이썬 답게 사용하는 방법을 배웠으면 좋겠다는 바람이다. pythonic 의 우아함에 감탄할때의 기쁨을
여러분이 놓치지 않기를 원하기 때문이다.


<h2>Let's Start Python</h2>
필자의 마음을 알아 주겠는가? 그러면 이제 다음 장으로 넘어가 보길 바란다.
 
<h2>20번째 계명</h2>
참고로 <a href="https://stackoverflow.com/questions/4504487/the-zen-of-python-distils-the-guiding-principles-for-python-into-20-aphorisms-bu">
20번째 계명
</a>은 여러분들이 만들어서 스스로의 마음에 하나씩 간직하고 있길 바란다. 어쩌면 파이썬을 배우는 도중에,
전문적으로 개발을 시작한 이후에 '20번째' 계명이 만들어질지도 모르겠다.