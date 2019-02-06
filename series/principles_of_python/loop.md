---
title:  "반복"
date:   2019-01-28 20:21:03 +0900
---


## 구구단을 외자
1단 부터 9단 까지 출력하는 프로그램을 만들어보자.
먼저 1단 부터 3단까지 출력하는 부분 먼저 작성해 보자.
{% highlight python %}
print(1*1)
# 작성해보기
{% endhighlight %}

<br><br>
혹시 1단 부터 3단까지의 코드를 작성하면서 불편함을 느꼈는가?
똑같은 문장을 반복하고 있다. 완전히 똑같은 것은 아니고 오른쪽 숫자만 1, 2, 3 이렇게 달라져서
하나씩 수정해 주어야 한다. 반복문을 배우기 전이라면
Ctrl + C, Ctrl + V 를 사용하는게 최선일지도 모른다.
{% highlight python %}
print(1*1)
print(1*2)
print(1*3)
print(1*4)
print(1*5)
print(1*6)
print(1*7)
print(1*8)
print(1*9)
{% endhighlight %}
코드를 일일이 복사/붙여넣기 하는 일은 번거롭다.
만약 이 상태에서 (그리고 9단까지 모두 작성한 상태에서)
{% highlight python %}
print('{} x {} = {}'.format(1, 1, 1)) # print(1*1)
print('{} x {} = {}'.format(1, 2, 2)) # print(1*2)
# ...
{% endhighlight %}
모든 코드를 위와 같이 수정해야 한다면? 이 또한 여간 번거로운 일이 아니다.



## for in을 사용한 구구단
반복문을 사용하면 위처럼 반복되는 작업을 복사/붙여넣기를 사용하지 않아도 된다.
그리고 나중에 반복되는 코드를 수정하는 것도 매우 쉬워진다. 
그럼 여기서 반복문 for in 문을 소개한다. 
아래의 간단한 반복문은 구구단 1단 1\*1 부터 9단 9\*9 를 전부 출력한다.

{% highlight python %}
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j)
{% endhighlight %}


## for in 문 (혹은 for문)
for 문의 구조를 설명하면,
{% highlight python %}
for <변수> in <iterable>
    # 코드 블럭, <변수>를 사용할 수 있다.
{% endhighlight %}
이렇게 되어 있다. 여기서 iterable 은 '각 요소를 순회할 수 있는 모든 것' 이라고 생각하면 된다.
<br><br>
파이썬 자판기를 만들 때를 기억하는가?
{% highlight python %}
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']
{% endhighlight %}
merchandise 도 iterable 이다. merchandise 안에는 각 음료수가 들어있고, for 문을 사용하면
각 음료수를 하나씩 순회할 수 있다. 
{% highlight python %}
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

for drink in merchandise:
    print(drink)
{% endhighlight %}
출력 결과:
```markdown
파워에이드
코카콜라
칠성사이다
게토레이
포카리스웨트
스프라이트
핫식스
```





## range
{% highlight python %}
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j)
{% endhighlight %}
for in 문의 작동방식에 대해서는 알았는데, range(1, 10) 는 어떤 역할을 할까?
함수 range() 에는 시작 값과 끝 값을 정해 줄 수 있다.
그리고 그 호출결과로 시작 값 부터 (끝 값 -1) 까지의 정수가 들어있는 iterable 을 받는다.
{% highlight python %}
for i in range(1, 10):
    print(i)
{% endhighlight %}

출력결과:
```markdown
1
2
3
4
5
6
7
8
9
```


## for 문의 중첩
for 문 안에서 for 문을 사용할 수 있다.





## while 을 사용한 반복
반복에는 for 이외에도 while 을 사용할 수 있다.
{% highlight python %}
while <조건식>:
    # 코드
    
{% endhighlight %}
while 은 iterable 을 순회하는 것이 아닌 조건식을 조사하는 방식으로 반복을 수행한다.
조건식이 참(True) 라면 while 코드 블럭이 실행되고, 거짓(False) 이라면 while 코드 블럭은
실행되지 않는다.

앞의 구구단 출력 문을 while 을 사용해서 표현하면 다음과 같다.
{% highlight python %}
i = 1
while i < 10:
    j = 1
    while j < 10:
        print(i*j)
        j+=1
    i+=1
{% endhighlight %}



## 무한 루프
우리가 사용하는 거의 모든 컴퓨터 프로그램에 무한루프가 들어간다.
예를 들어 핸드폰 어플리케이션도 
웹 서버도 무한 루프의 일종이다.





## 연습문제
반복을 사용해서 9단의 9\*9 부터 1단의 1\*1 까지 거꾸로 구구단을 출력하는 프로그램을 만들어 보자.


## 다시 가위 바위 보
n 선승제의 가위바위보 게임을 만들어보자.
가위바위보를 입력받는 방식은 '조건문'에서 배웠던 방식과 똑같다.
게임을 시작하기 전에 몇 번 먼저 이긴 사람이 승자가 될 지 정수로 입력받는다.
승자가 결정되면 바로 승자를 출력하고, 프로그램을 종료한다.















