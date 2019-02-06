---
title:  "노래하는 파이썬"
date:   2019-01-31 20:21:03 +0900
---


## Hello World!
새로운 파일 hello.py 를 생성한 뒤, 다음과 같이 파일의 내용을 채워보자.
{% highlight python %}
print('hello world')
{% endhighlight %}
실행하면 화면에 hello world 가 출력된다면 성공이다. 여러분은 방금 파이썬을 사용해
첫 프로그램을 실행 시킨 것이다.

## Hello GangNam Style
화면에 hello world 만 출력되는 건 조금 심심하지 않은가?
앞서 작성했던 내용은 지워버리자.
<br><br>
파이썬 강남스타일을 소개한다.
아래의 내용을 복사해서 hello.py 안에 붙여넣자.
그러면 파이썬이 연주하는 익숙한 강남 스타일 멜로디가 흘러나올 것이다.
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

파이썬을 사용하면 이처럼 강남스타일도 연주할 수 있다.
이제 다음 장으로 넘어가자.

파이썬 강남 스타일 링크
<a target="_blank" href="https://codeboom.wordpress.com/2012/10/11/python-gangnam-style/">
https://codeboom.wordpress.com/2012/10/11/python-gangnam-style/</a>