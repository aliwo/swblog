---
title:  "super 와 diamond 문제"
date:   2019-01-28 20:21:03 +0900
---


## 짬짜면

짜장면, 짬뽕은 모두 '면' 과 is a 관계가 성립한다.
 
{% highlight python %} 
class Noodle: # 면 클래스 Noodle

    def __init__(self):
        self.ingredients = ['면'] # 모든 면 류 음식의 기본 재료는 '면


class Zza(Noodle): # 짜장면 클래스 Zza
    
    def __init__(self):
        Noodle.__init__(self)
        self.ingredients.append('춘장') # 짜장 = 면 + 춘장


class Zzam(Noodle): # 짬뽕 클래스 Zzam
    
    def __init__(self):
        Noodle.__init__(self)
        self.ingredients.append('고추가루') # 짬뽕 = 면 + 고추가루


class ZzamZza(Zza, Noodle): # 짬짜면 클래스 Zzam
    
    def __init__(self):
        Zza.__init__(self)
        Zzam.__init__(self)

{% endhighlight %}


## 짬짜면의 재료는?
이연복 선생님 께서 보시면 경악을 금치 못할 재료 구성이지만, 공부를 위해
각 요리의 재료 구성을 단순화 시켜 보았다. 자 이제 짬짜면 클래스를 인스턴스화 하면
그 재료는 어떻게 될까? 아마도

**['면', '춘장', '고추가루']**
{: .text-center}

이 될 것이다. 확인해보자.
{% highlight python %} 
# 초략

my_dinner = ZzamZza()
print(my_dinner.ingredients) ['면', '고추가루'] # ? 춘장 어디갔어

{% endhighlight %}

## 다이아몬드 문제
춘장이 어디론가로 없어졌다. 예상치 못한 결과가 나온 것이다.
왜 위와 같은 문제가 일어나는 것일까? 원인은 자녀 클래스를 인스턴스화 할 때 생성자가 호출되는 순서에
있다. 짬짜면 클래스는 자신의 생성자에서 다음과 같은 순서대로 부모 클래스의 생성자를 호출했다.
1. 짜장면 클래스의 생성자 호출
2. 짬뽕 클래스의 생성자 호출
이 때 면 클래스의 자녀(짜장, 짬뽕)들은 저마다 면 클래스의 생성자를 호출한다. 
따라서 짬짜면 클래스의 생성자 내부에서 실제로 일어나는 일은 다음과 같다.

**면 클래스의 생성자 호출(짜장면의 부모) -> 짜장면 클래스의 생성자 호출 
-> 면 클래스의 생성자 호출(짬뽕의 부모) -> 짬뽕 클래스의 생성자 호출**
{: .text-center}

때문에 각 단계별로 멤버변수 `self.ingredient` 는 다음과 같이 변한다.

**['면'] -> ['면', '춘장']  -> ['면'] -> ['면', '고추가루']**
{: .text-center}

즉, 면 클래스의 생성자가 2번 호출되기 때문에 예상치 못한 결과가 발생한 것이다.

## 부모 클래스의 생성자를 호출 할 땐 super 를 사용하자!

상속 관계의 모양이 다이아 몬드 같은 상태에서 발생하는 문제기 때문에 
위와 같은 문제를 다이아몬드 문제라고 한다. 프로그래밍 언어마다 다이아몬드 문제를 해결하는
방법은 다양하다. 예를 들어 java 의 경우에는 아예 다중 상속을 허용하지 않는 방법을 사용하고 있다.

파이썬의 다이아몬드 문제 해결방법은 super 다.

참고: 함수 이름이 super 인 이유는 이 함수가 짱짱 좋은 함수 여서가 아니라, 
부모 클래스를 super class 라고 부르기 때문이다.







