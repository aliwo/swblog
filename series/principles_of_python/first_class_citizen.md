---
title:  "First Class Citizen"
date:   2019-01-24 09:21:03 +0900
---


## 함수도 일종의 자료형 입니다.
함수를 호출할 때에는 함수 이름에 ()소괄호를 붙인다고 했었다.
그렇다면 소괄호를 안 붙이면 어떻게 될까? 에러가 날까?
{% highlight python %}
def get_number_7():
    return 7

who_are_you = get_number_7 # who_are_you 에는 무엇이 할당될까?
{% endhighlight %}

(놀랍게도) 아무런 에러도 일어나지 않았다.
여기서 코드 한 줄만 추가해 보겠다.
{% highlight python %}
def get_number_7():
    return 7

who_are_you = get_number_7 # who_are_you 에는 무엇이 할당될까?
print(who_are_you()) # 7 출력
{% endhighlight %}

변수 who_are_you 를 호출했더니, get_number_7 을 호출한 것과 같은 값이 나왔다.
무슨 일이 일어난 것일까?

## 따라서 함수를 할당할 수 있습니다.
변수 who_are_you 에는 함수 get_number_7이 할당된 것이다.
함수도 일종의 자료형이다. 우리가 자주 사용하는 int(정수), str(문자열) 처럼 함수도 
메모리 공간을 차지하고 있다. 정수나 문자열을 변수에 할당하는 것 처럼 함수도 얼마든지 변수에 할당할 수 있다.
그 방법은 바로 소괄호를 붙이지 않고 함수 이름만 적는 것이다. 
{% highlight python %}
<변수 이름> = <함수 이름>
my_function = get_number_7
{% endhighlight %}
함수는 호출되지 않고, 함수 그 자체로 변수에 할당된다.

## First Class Citizen
파이썬에서 말하는 일급 시민(Fist Class Citizen), 혹은 일급 객체의 조건은 다음과 같다.
다음 4가지 조건을 만족시키면 곧 일급 시민이다.
* 함수의 입력으로 들어갈 수 있다.
* 함수의 결과값으로 리턴될 수 있다.
* 변수에 할당될 수 있다.
* 리스트, 집합(set) 등의 컨테이너 자료형 안에 담길 수 있다.

따라서 파이썬의 모든 함수는 FIrst Class Citizen 이다.






