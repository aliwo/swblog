---
title:  "노래하는 파이썬"
date:   2019-01-31 20:21:03 +0900
---


## Hello World!

{% highlight python %}

{% endhighlight %}


## Hello GangNam Style


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


파이썬 강남 스타일 링크
<a target="_blank" href="https://codeboom.wordpress.com/2012/10/11/python-gangnam-style/">
https://codeboom.wordpress.com/2012/10/11/python-gangnam-style/</a>