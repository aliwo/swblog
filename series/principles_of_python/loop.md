---
title:  "반복"
date:   2019-01-28 20:21:03 +0900
---


## 구구단을 외자
구구단의 1단 부터 9단 까지 순서대로 출력하는 프로그램을 만들어야 한다면 여러분은 어떻게 하겠는가?
먼저 1단 부터 3단까지 출력하는 부분을 어떻게 구현할지 생각해 보자.
{% highlight python %}
print(1*1)
# 스스로 작성해보기
{% endhighlight %}

<br><br>
다 작성했는가? 혹시 1단 부터 3단까지의 코드를 작성하면서 불편함을 느꼈는가?
똑같은 문장을 반복하고 있다는 느낌이 들지는 않았는가? 
완전히 똑같은 것은 아니고, a * b 에서 b가 1씩 증가하는 모양이다.
b가 1씩 증가하기 때문에 print()문을 복사 붙여넣기(Ctrl + C, V)를 하고 나서
b 값을 일일히 수정해 주어야 한다는 불편함을 겪었을 것이다.
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
print 문을 복사해서 숫자만 바꿔치는 작업은 심각한 문제가 있다. 매우 번거롭고, 지루하다는 것이다.
만약 이 상태에서 (그리고 9단까지 모두 작성한 상태에서)
{% highlight python %}
print('{} x {} = {}'.format(1, 1, 1)) # print(1*1)
print('{} x {} = {}'.format(1, 2, 2)) # print(1*2)
# ...
{% endhighlight %}
모든 코드를 위와 같이 수정해야 한다면? 
81 개의 print 문을 일일이 수정해 주어야 한다!

## 반복문의 필요성
print() 함수를 81번 복사해서 늘어놓기 보다는,
아래와 같은 명령을 사용할 수 있다면 좋을 것 같아 보인다.

```markdown
1. 변수 a에 순서대로 1부터 9까지 할당한다.
    2. a에 숫자를 하나 할당할 때 마다 b에 1부터 9까지 할당한다.
        3. print(a * b)
```

만약 위 명령문 처럼 print() 문 하나로 반복작업을 수행할 수 있다면
나중에 print() 안의 내용을 수정하는 것도 전보다 훨씬 편할 것이다.

1번과 2번 명령문은 반복 작업(변수를 순서대로 할당하는 일)을 요구한다.
반복 작업을 수행하는 문장을 반복문 이라고 한다.

## for in을 사용한 구구단
반복문을 사용하면 위처럼 반복되는 작업이 필요할 때 복사/붙여넣기를 사용하지 않아도 된다.
그리고 나중에 반복되는 코드를 수정하는 것도 매우 쉬워진다.
즉 반복문을 사용하는 것이 작업 속도 면에서나, 유지보수 측면에서나 '더 우아한' 방법이라고 말할 수 있다.
<br><br>
그럼 여기서 반복문 for in(줄여서 for 문) 을 소개한다. 
아래의 간단한 반복문은 구구단 1단 1\*1 부터 9단 9\*9 를 전부 출력한다.
한 번 실행해보자.
{% highlight python %}
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j)
{% endhighlight %}


## for 문의 작동방식 (혹은 for문)
for 문의 구조는 다음과 같다.
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

for 문을 사용해서 merchandise 목록의 요소들을 하나씩 나열해 보았다.
for 문은 이처럼 iterable 안의 요소를 하나씩 <변수> 에 할당하면서
for 문 블럭 안의 반복작업을 수행한다.



## range
다시 구구단을 출력하는 코드로 돌아가자.
{% highlight python %}
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j)
{% endhighlight %}
for in 문의 작동방식에 대해서는 알았는데, range(1, 10) 는 어떤 역할을 할까?
함수 range() 에는 시작 값과 끝 값을 정해 줄 수 있다.
그리고 그 호출결과로 시작 값 부터 '끝 값 -1' 까지의 정수가 들어있는 iterable 을 
결과값으로 내보낸다.

{% highlight python %}
my_iterable = range(1, 10)
my_iterable # 정수 1 부터 9 까지가 들어있는 iterable 
{% endhighlight %}

끝 값(10)이 아닌 끝 값 -1 (9) 까지만 반복하는게 이상하게 느껴지겠지만,
이는 다른 파이썬 함수들과의 조화를 맞추기 위해서이다. (list 자료형을 배울 때 알아볼 것이다.)
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


## break 반복 탈출

다음은 merchandise 음료수 목록 중에서
포카리스웨트가 존재하는지를 검사하는 코드이다.
만약 포카리스웨트가 존재하면 found 변수를 True 로 만든다.
{% highlight python %}

merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

found = False
for drink in merchandise:
    if drink == '코카콜라':
        found = True
 
 if found:
    print('포카리 스웨트가 있어요.')
{% endhighlight %}
코드의 목적은 코카콜라가 상품목록에 있는지 찾는 것인데, 일단 코드 자체는 잘 작동한다.
하지만 한 가지 낭비를 하고 있다. 코카콜라를 찾았다면 더 이상 for 문을 반복할 필요가 없지만 
코카콜라를 찾고 나서도 반복을 계속한다는 것이다.

더 이상 반복할 필요가 없을 때에는 키워드 break 를 사용해서 반복문을 빠져나오면 된다.
{% highlight python %}

merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

found = False
for drink in merchandise:
    if drink == '코카콜라':
        found = True
        break # 반복문 탈출!
 
 if found:
    print('포카리 스웨트가 있어요.')
{% endhighlight %}



## 연습문제
반복을 사용해서 9단의 9\*9 부터 1단의 1\*1 까지 거꾸로 구구단을 출력하는 프로그램을 만들어 보자.


## 다시 가위 바위 보
n 선승제의 가위바위보 게임을 만들어보자.
가위바위보를 입력받는 방식은 '조건문'에서 배웠던 방식과 똑같다.
게임을 시작하기 전에 몇 번 먼저 이긴 사람이 승자가 될 지 정수로 입력받는다.
승자가 결정되면 바로 승자를 출력하고, 프로그램을 종료한다.















