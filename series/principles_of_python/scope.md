---
title:  "변수의 스코프"
date:   2019-08-06 10:21:03 +0900
---

## 서울의 김씨와 부산의 김씨
스코프에 대해 설명하기 위해 잠깐 초코 공장으로 부터 벗어나 깜짝 퀴즈를 하나 내려고 한다: 
서울 특별시 강남구 개포동에 사는 김씨와 부산광역시 동래구 낙민동에 사는 김씨는
서로 같은 사람일까?

답은? 당연히 아니다. 성이 같다고 해서 같은 사람은 아니다. 
같은 사람이라면 어떻게 서로 다른 지역에 공존하겠는가?
사람은 편재하지 않는 걸.

그럼 다시,

아래의 파이썬 코드에서 function_seoul 의 변수 kim 과
function_busan 의 변수 kim 은 같은 변수일까 서로 다른 변수일까?

{% highlight python %}
def function_seoul():
    kim = '서울의 김씨'
    print(kim)

def function_busan():
    kim = '부산의 김씨'
    print(kim)
{% endhighlight %}

2개의 kim은 서로 다른 변수이다. 이들은 이름이 같다는 것을 제외하면 연관이 없다.
실제로 function_seoul 안에서 아무리 kim 을 선언해도, function_busan 에서는
그 사실 조차 알지 못한다.

{% highlight python %}
def function_seoul():
    kim = '서울의 김씨'
    kim = '서울에 김씨가 있어요!'
    print(kim)

def function_busan():
    print(kim) # 부산에는 김씨가 없는데요?
    
function_busan() # NameError: name 'kim' is not defined
{% endhighlight %}

function_busan() 으로 부산 함수를 호출해 보면 에러가 발생한다.
busan 에서는 seoul 의 kim 씨를 찾을 수 없기 때문이다.
방금 시연해 본 것 처럼 변수에게는 저마다의 활동 구역이 존재하는데, 이를 변수의 스코프(scope) 라고 한다.

스코프의 정의는 다음과 같다.

**변수가 존재할 수 있는 영역, 혹은 변수에 접근할 수 있는 영역**
{: .text-center} 


## global scope 와 local scope 
엄밀히 따지고 들어가면 여러 종류의 scope 가 있지만,
대부분의 경우에는 딱 2개의 scope 만 생각하면 된다.
하나는 Global Scope 이고, 다른 하나는 Local Scope 이다.
앞서 봤던 seoul 과 busan 의 비유는 Local Scope 를 설명한 것이라고 볼 수 있으니,
이번에는 Global Scope의 예를 들어보겠다.

김대통령을 만나보시라.

{% highlight python %}
kim = '김 대통령'
def function_seoul():
    print(kim)

def function_busan():
    print(kim)
{% endhighlight %}

함수 안이 아니라 함수 밖에서 kim 을 선언했다.
이 kim 은 (너무 유명해서) 서울에서도 kim 이라고 하면 김 대통령인 줄 알고
부산에서도 kim 이라고만 하면 바로 김 대통령인 줄 안다.

이처럼, Global Scope 에서 선언된 변수는
Local Scope 인 함수 안에서도 접근할 수 있다.
Global 이라는 이름에 맞게, 어디에서든지 접근할 수 있다.

Global Scope 에서 선언된 변수를 '전역변수' 라고 부른다.
따라서 `kim = '김대통령'` 의 `kim` 은 전역변수이다.
반대로 local scope 의 변수를 '지역변수' 라고 부른다.

## Local Scope 가 만들어질 때
Local Scope 의 바깥은 무조건 Global Scope 라고 기억해 두면 편하다.
(엄밀히 말해서 딱 2개의 Scope 만 있는 건 아니지만)

그렇다면 Local Scope 는 언제 만들어지는 것일까?
방금 서울과 부산의 예에서 봤듯, 함수안에서 Local Scope 가 만들어진다.
또한 나중에 배우게 될 Class 에서 또한 Local Scope 가 만들어진다.

정리하자면 Local Scope 가 만들어지는 때는 다음 2가지다.
* 함수
* 클래스


## 이 구역의 kim은 나야
그럼 이제 kim 을 알아 맞춰보는 연습을 해 보자. 하다보면 익숙해진다.

{% highlight python %}
kim = '김대통령'
def function_seoul():
    print(kim)

def function_busan():
    print(kim)
    
function_seoul()
function_busan()
{% endhighlight %}

출력결과는 다음과 같다. 

```
김대통령
김대통령
```

다음 문제.

{% highlight python %}
kim = '김 대통령'
def function_seoul():
    kim = '서울의 김씨' # 서울에서 kim 을 다시 정의해요.
    print(kim)

def function_busan():
    print(kim)
    
function_seoul()
function_busan()
{% endhighlight %}

출력결과는 다음과 같다. 

```
서울의 김씨
김대통령
```

function_seoul() 이 '서울의 김씨' 를 출력한 이유를 알아보자.

파이썬 인터프리터는  `kim = '서울의 김씨'` 를 해석할 때, 이미 전역변수 kim 이 존재한다는
것을 알고 있다. 이때 전역변수 kim 의 값을 바꾸는 대신, function_seoul() 안에만 존재하는
지역변수 kim 을 '새로' 만든다. 
{% highlight python %}
kim = '김 대통령' # function_seoul 에 의해서 변하지 않아요.
def function_seoul():
    kim = '서울의 김씨' # 이 kim 은 지역변수 kim 입니다.
    print(kim)
{% endhighlight %}
때문에 전역변수 kim 은 변하는 일 없이 계속 '김 대통령' 인 것이다.
  
function_seoul() 안에서 정의된 kim 은 function_busan() 과는 아무 관련이 없다고 했다.
한 편, function_busan() 안에서는 어떠한 kim 도 새로 정의되지 않으므로 전역변수 kim 을 가져다 쓴다.
그 값은 변하지 않고 '김 대통령' 이다.

다음문제. 지역 스코프에서 전역변수를 수정하려고 하면 어떻게 될까?



## 변수 Best Practice
그렇다면 지역변수와 전역변수는 어떻게 사용하는게 올바른 방법일까?
* 전역변수는 최대한 줄인다.
* 전역변수와 이름이 똑같은 지역변수는 되도록이면 지양한다.





## 정리하기
이번에 변수의 스코프 에 대해서 배운 내용을 정리하자면 다음과 같다.

* 변수는 저마다의 활동영역이 있다. 이를 변수의 스코프 라고 부른다.
* 일단은 Global Scope, Local Scope 만 신경 쓰자. (이외에도 Built-in, Enclosed 등이 있다.) 
* 서로 다른 영역의 변수는 설령 이름이 같을지라도 서로 다른 변수이다.
* 같은 이름의 전역변수가 있을 지라도, 함수 안에서는 지역 변수가 새로 생성된다.
* 지역 스코프 에서는 전역변수를 수정할 수 없다.

## Scope 는 왜 필요한 거죠?
스코프가 뭐 하는 녀석인지 열심히 배우기는 했는데,
어쩌면 "이런 복잡한 규칙을 왜 만든걸까?" 라고 생각이 들 지도 모르겠다.
그래서 다시 초코 공장으로 돌아가서 설명해 보려고 한다.
다음 챕터에서 Scope 가 필요한 이유를 간단히 짚고 넘어가자.


## 참고
본문에서는 Local Scope 가 만들어지는 경우를 함수와 클래스 라고 정리하긴 했지만,
실제로는 더 있다. List Comprehension 이라고 하는 기능도 스코프를 만든다.
하지만 크게 신경 쓸 필요는 없다.

파이썬에서 스코프 안의 이름을 찾는 규칙을 LEGB Rule 이라고 한다.
더 공부하고 싶다면 구글에서 검색해 보면 된다. 각 약자는 Local, Enclosed, Global, Built-in 을 의미한다.





















