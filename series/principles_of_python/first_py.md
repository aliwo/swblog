---
title:  "노래하는 파이썬"
date:   2019-01-31 20:21:03 +0900
---


## Hello World!
성경이 "태초에 하나님이 천지를 창조하시니라"로 시작한다면
프로그래밍 언어를 배우는 것은 `Hello World` 출력 으로 시작한다. 
왜 하필이면 Hello World 인지는 아래의 나무위키 링크를 참고하자.

여러분의 IDE 에서 새로운 파일 hello.py 를 생성한 뒤, 
다음과 같이 파일의 내용을 채워보자.
{% highlight python %}
print('hello world')
{% endhighlight %}
실행했을때 화면에 hello world 가 보인다면 성공이다.
이처럼 화면에 글자를 내보내는것을 `출력한다` 라고 한다.

## Hello GangNam Style
화면에 hello world 만 출력되는 건 조금 심심하지 않은가?
앞서 작성했던 내용은 지워버리고, 이번엔 GangNam Style 을 한번 출력해 보겠다.
<br><br>
파이썬 강남스타일을 소개한다.
아래의 내용을 복사해서 `hello.py` 안에 붙여넣자.
실행하면 파이썬이 연주하는 익숙한 강남 스타일 멜로디가 흘러나올 것이다.
참고로 윈도우 사용자만 가능하니, mac 이나 리눅스 사용자에게는 양해를 구한다. 

{% highlight python %}

import winsound
import time

winsound.Beep(293, 200) # D
winsound.Beep(293, 200) # D
winsound.Beep(293, 200) # D
winsound.Beep(293, 600) # D
winsound.Beep(246, 600) # B

time.sleep(0.1)

winsound.Beep(369, 200)# F#
winsound.Beep(369, 200)# F#
winsound.Beep(369, 200)# F#
winsound.Beep(369, 600)# F#
winsound.Beep(329, 600) # E

time.sleep(0.1)

winsound.Beep(329, 200) # E
winsound.Beep(329, 200) # E
winsound.Beep(329, 200) # E
winsound.Beep(369, 500) # F#

time.sleep(0.9)

winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#
winsound.Beep(369, 600) # F#

time.sleep(0.9)
winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#
winsound.Beep(369, 200) # F#

for i in range(4):
    winsound.Beep(369, 200) # F#
    time.sleep(0.1)

for i in range(4):
    winsound.Beep(369, 100) # F#
    time.sleep(0.1)

winsound.Beep(369, 600) # F#

# PYTHON GANGNAM STYLE!
{% endhighlight %}

import 는 무엇을 의미하는지, 
time.sleep(0.9)는 무슨 의미인지, 어떻게 해서
강남스타일의 멜로디가 연주되는지 궁금해 졌을것 같다.
앞으로 차근차근 배우게 될 것이고, 어느 순간에는
위 코드가 전부 이해가 될 것이다. 이제 다음 장으로 넘아가 보자.

파이썬 강남 스타일 코드의 링크:
<a target="_blank" href="https://codeboom.wordpress.com/2012/10/11/python-gangnam-style/">
https://codeboom.wordpress.com/2012/10/11/python-gangnam-style/</a>


## 참고
<a target="_blank" href="https://namu.wiki/w/Hello,%20world!">
헬로우 월드 나무위키
</a>
