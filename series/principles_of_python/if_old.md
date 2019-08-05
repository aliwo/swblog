---
title:  "조건문"
date:   2019-02-22 20:21:03 +0900
---

## 만약
또 라면 이야기다.
앞서 배웠던 저녁 메뉴 정하기를 if 조건문을 사용해서 표현해 보겠다.

{% highlight python %}
# 삼항 연산자 버전
lunch_menu = '라면'
dinner = '돈까스' if lunch_menu == '라면' else '라면'
print(dinner) # '돈까스' 출력

# if 조건문 버전
if lunch_menu == '라면':
    dinner = '돈까스'
else:
    dinner = '라면'
print(dinner) # '돈까스' 출력
{% endhighlight %}

삼항 연산자 버전, if 조건문 버전 둘은 똑같은 기능을 한다. 점심이 라면 이었다면
저녁은 돈까스를 먹고, 점심이 라면이 아니었다면 저녁은 라면으로 떼운다.

## if 조건문의 구조

{% highlight python %}
if <조건문1>:
    # 코드블럭1
{% endhighlight %}

if는 어떤 조건문이 '참' 일 때에만 코드를 실행해야 하는 경우에 사용한다.

if 조건문을 쓸 때에는 if 키워드 다음에 한 칸을 띄어쓰고, 
조건문을 작성한 뒤 콜론: 으로 끝을 맺는다.
if 다음에 오는 코드블럭은 한 칸 들여쓴다. 
들여 쓸 때에는 스페이스바 4개를 사용하는데,
pycharm 을 사용하고 있다면 그냥 tab을 누르면 된다. pycharm 이 
알아서 tab 문자를 스페이스바 4개로 바꿔준다.

{% highlight python %}
if lunch_menu == '라면': # 점심에 이미 라면을 먹었다면
    dinner = '돈까스' # 저녁은 돈까스로 하자.
{% endhighlight %}

if 조건문을 작성하는 줄에서는 들여쓰기를 하지 않음에 주의하자.
if 키워드 다음의 코드블럭부터 들여쓰는 것이다.

{: .text-center}


## if 와 else
{% highlight python %}
if lunch_menu == '라면':
    dinner = '돈까스'
else:
    dinner = '라면'
{% endhighlight %}

if 문이 '거짓' 일 때 어떤 코드를 실행하고 싶다면 else 문을 사용하면 된다.
else 문은 if 문이 끝난 바로 다음 줄에 작성하면 된다.
else: 로 시작하며, 조건식은 필요 없다. (if 문이 거짓이 되는 것 자체가 조건이기 때문이다.)
else: 다음 줄은 한 번 들여쓴다.

본문에서는 lunch_menu 가 '라면' 일때 if 블럭이 실행되며, 만약 '라면' 이 아니라면
else 블럭이 실행된다.


## if 와 else 와 elif

**elif** 라는 키워드도 있다.
elif는 else if 의 줄임말 이다. 첫번째 if 가 False 일 때, 
또 다른 조건을 다시 걸고 싶다면 elif를 사용한다.

추가적인 조건을 달 수 있는 else 문이라고 생각하면 된다.

{% highlight python %}
if <조건문1>:
    # 코드블럭1
elif <조건문2>:
    # 코드블럭2
else:
    # 코드블럭3 
{% endhighlight %}

* if 조건문의 조건문1 이 True 라면 코드블럭1이 실행되며
* 조건문1은 False 이지만 조건문2가 True 라면 코드블럭2가 실행되며
* 조건문1과 2 모두 False 이면 코드블럭3 이 실행되는 방식이다.


## 피카츄(은)는 무엇을 할까?
if 안에 또 if 를 쓰는 것도 가능하다. 이를 **if 문을 중첩한다** 라고 한다.
예를 들어 포켓몬 대전 게임을 수행하는 알고리즘을 만든다고 하자.
자신의 체력이 낮아졌을때,
* 필살기 백만볼트의 PP가 남아있다면 백만볼트를 사용한다. (pp가 뭔지 모른다면 
<a href="https://namu.wiki/w/%EB%B0%9C%EB%B2%84%EB%91%A5" target="_blank">여기</a>)
* 남아있지 않다면 도망친다. 


되도록이면 if문을 작성하는 연습을 위해 복사 / 붙여넣기 없이 직접 아래의 코드를 타이핑 해서 실행해보자.

{% highlight python %}
hp = 9
power_point = 1
next_move = ''
if hp < 10: # 체력이 낮다!
    if power_point != 0:
        next_move = '필살기 사용'
    else:
        next_move = '도망쳐'
{% endhighlight %}


## if 를 중첩하지 말자.
if 를 3 겹 이상 중첩하게 되면 극도로 읽기 어려운 코드가 만들어진다.



## 연습문제: 가위 바위 보
두 사람이서 가위바위보를 하는 프로그램을 만들어보자.
플레이어 A와 B가 있다고 할 때, A가 먼저 가위, 바위, 보 중 하나를 고르고
그 다음 자리를 비킨다. B가 이어서 가위, 바위, 보를 고르고
B가 골랐다면 바로 각 플레이어가 고른 가위,바위,보 를 출력하고,
승자가 누구인지 출력한다. (비겼다면 비겼음을 출력한다.)

어디서 부터 시작할지 막막하다면 아래 코드를 읽어보고, 이어져야 하는 코드블럭을 작성해보자.
물론 읽어보지 않고 스스로 시작해 보는 것을 더 권장한다.
<br><br><br>


{% highlight python %}
rock = '바위'
scissor = '가위'
paper = '보'

player_a = '플레이어 A'
player_b = '플레이어 B'
{% endhighlight %}

