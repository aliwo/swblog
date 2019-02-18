---
title:  "생성자"
date:   2019-02-18 13:21:03 +0900
---

## 행버거를 만들어보자.

다음과 같은 햄버거 클래스가 있다고 하자.
집ㄱ...버거 라고 하고 싶지만 저작권이 무서운 관계로 그냥 버거라고 하겠다. 

{% highlight python %}
class Burger:
    ingredients = ['bun', 'patty', 'lettuce', 'tomato', 'pickle']
    taste = 5 # 5 out of 5
    
{% endhighlight %}

생성한 버거 클래스로 부터 버거 객체를 문제없이 만들 수 있다.


{% highlight python %}
class Burger:
    ingredients = ['bun', 'patty', 'lettuce', 'tomato', 'pickle']
    taste = 5 # 5 out of 5

my_burger = Burger()
{% endhighlight %}

## 모든 버거를 똑같이 만들 수 있을까?
현실적으로 생각해 보자. 아무리 패스트 푸드 체인점에서 만든 버거라 해도
그 맛이나 내용물이 전부 똑같지는 않다. 아주 가끔은 종업원이 실수로 패티를 태울 수도 있고,

아니면 손님이 자신의 버거에는 피클을 빼달라고 요청할 수도 있다. 가끔은 맛이 조금
떨어지는 버거가 나올 수 있다. 
즉 같은 Burger 형 객체일 지라도 객체마다 그 내용물이 조금씩 달라질 수 있다는 뜻이다.
따라서 방금 만든 버거 클래스에 현실성을 가미해 보도록 하겠다.


## 생성자

{% highlight python %}
class Burger:
    ingredients = ['bun', 'patty', 'lettuce', 'tomato', 'pickle']
    taste = 5 # 5 out of 5

    def __init__(self, pickle):
        if pickle is False: # pickle 은 True or False 값이다.
            self.ingredients.remove('pickle')

my_burger = Burger(True) # 피클이 들어있는 버거
print(my_burger.ingredients)

my_burger_without_pickle = Burger(False) # 피클이 없는 버거
print(my_burger_without_pickle.ingredients)
{% endhighlight %}

여러분에게 특별한 메소드를 하나 소개한다. 이 메소드는 그 이름을 __init__ 이라 적고
부를 때에는 '생성자'(constructor) 라고 부른다. (init 메소드라고 부르는 경우도 가끔 있다.)


생성자는 그 단어 그대로, 객체를 생성하는 임무를 맡고 있다. 여러 메소드 들 중에서도
특별한 메소드로, 클래스로부터 객체가 생성될때 반드시 호출된다는 특성을 가지고 있다.

* 생성자 안에는 보통 멤버 변수를 설정하는 코드를 넣어준다.
* 생성자 안에서는 return 을 사용하지 않는다. 만약 사용한다 해도 의미가 없으며, None 을 리턴하지 않는다면
에러가 난다.
* 메소드 이름은 반드시 __init__ 으로 한다.

여러분이 `my_burger = Burger()` 를 호출 할 때 내부적으로는 __init__() 이 호출되고, 
__init__() 이 완료 된 이후 my_burger 에 Burger 객체가 할당된다.



## 보통은 피클을 넣어서 먹더라구요
패스트 푸드점의 매니저가 한 가지 문제를 발견했다. 손님들은 대부분 피클이 있는 버거를 선호하는데,
버거를 만들 떄 마다 `Burger(True)` 혹은 `Burger(False)`로 피클을 넣을지 
여부를 알려주어야 하니, 불편하다는 것이다.

`Burger()` 는 피클이 있는 버거를 만들고, 피클을 원하지 않을 때에만 `Burger(False)` 를 
호출하도록 만들 수는 없을까?


{% highlight python %}

    def __init__(self, pickle=True): # 디폴트 파라미터!
        if pickle is False:
            self.ingredients.remove('pickle')

{% endhighlight %}

default parameter 를 사용하면 문제를 간단히 해결할 수 있다. 디폴트 파라미터는
변수를 할당하는 것 처럼 파라미터 오른쪽에 = 과 값을 넣으면 디폴트 파라미터를 만들 수 있다.

위에서는 pickle 값이 디폴트 값으로 True 를 사용하도록 하였다.

만약 생성자가 호출 될 때 파라미터 pickle 이 제시되지 않았다면, 
파이썬은 자동으로 디폴트 값인 True 를 사용한다.

{% highlight python %}
class Burger:
    ingredients = ['bun', 'patty', 'lettuce', 'tomato', 'pickle']
    taste = 5 # 5 out of 5

    def __init__(self, pickle=True): # 디폴트 파라미터!
        if pickle is False:
            self.ingredients.remove('pickle')

my_burger = Burger() # 피클이 들어있는 버거
print(my_burger.ingredients)

my_burger_without_pickle = Burger(False) # 피클이 없는 버거
print(my_burger_without_pickle.ingredients)
{% endhighlight %}

다음과 같이도 호출할 수 있다.
{% highlight python %}
my_burger_without_pickle = Burger(pickle=False)
{% endhighlight %}

디폴트 파라미터를 또다른 이름으로 **keyword argument** 라고 부를 때도 있다. 기억해 두자.






