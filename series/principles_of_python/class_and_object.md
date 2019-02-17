---
title:  "객체와 클래스"
date:   2019-01-24 09:21:03 +0900
---


## 객체와 클래스의 정의
객체는 '사물'을 의미한다. 
클래스는 '객체를 만들어 내는 설계도' 이면서 '객체의 종류'를 의미한다.


## 클래스 정의하기
클래스를 정의하려면 <br> 

class <클래스 이름>:
{: .text-center} 

이후에 한 번 들여쓴다. 
일단은 가장 간단한 형태의 스폰지밥 자료형 SpongeBob 클래스를 만들어 보겠다.
pass 는 '아무것도 하지 않는다' 라는 뜻의 키워드다.

{% highlight python %}

class SpongeBob:
    pass

{% endhighlight %}


## 클래스 변수 할당

클래스에는 클래스 멤버변수라는 변수를 할당할 수 있다. 
이 멤버변수는 클래스가 가지고 있는 속성을 나타낸다.

들여쓰고 나서 평소에 변수를 할당하던 것 처럼 할당한다.

{% highlight python %}
class SpongeBob:
    figure = '네모 모양'
    pants = '네모 바지'
    neck_tie = True
{% endhighlight %}

모든 스폰지밥은(스폰지밥, 그림밥, 파이썬밥) 모두 네모 모양이고, 네모 바지에, 넥타이를 입도록 정의했다.

## 인스턴스화
클래스로부터 객체를 만들어 내는 것을 인스턴스화(혹은 객체화) 라고 한다.
함수를 호출할 때 처럼 클래스 이름 오른쪽에 () 를 붙이면 인스턴스화 할 수 있다.
 
{% highlight python %}

class SpongeBob:
    figure = '네모 모양'
    pants = '네모 바지'
    neck_tie = True

my_spongebob = SpongeBob() # 스폰지밥 객체를 생성한다. 
{% endhighlight %}