---
title:  "객체와 클래스"
date:   2019-02-17 09:21:03 +0900
---


## class
class 는 우리가 여러차례 type() 함수를 사용하면서 늘 보던 단어다.

{% highlight python %}
>>> type([1, 2])
<class 'list'>
{% endhighlight %}


## 객체와 클래스의 정의
전에 자료형을 배우기 전 '객체' 챕터에서 객체는 곧 사물과 같다고 했었다. 
클래스는 '객체의 종류'(즉, 자료형)을 의미하는데, 동시에 '객체를 만들어 내는 설계도' 이기도 하다.
나머지는 코드를 보면서 이해하도록 하자.

## 클래스 정의하기
클래스를 정의하려면 다음과 같이 한다.
일단은 가장 간단한 형태의 스폰지밥 자료형 SpongeBob 클래스를 만들어 보겠다.
참고로 pass 는 '아무것도 하지 않는다' 라는 뜻의 키워드다.

pycharm 을 열자. 새로운 파일 sponge_bob.py 를 작성해 다음과 같이 채워 넣자.
{% highlight python %}
# sponge_bob.py
class SpongeBob:
    pass

{% endhighlight %}

## 클래스로부터 객체를 만들기
함수를 호출하는 것 처럼 소괄호를 사용해서 클래스 SpongeBob 을 호출하면 SpongeBob 객체를
얻을 수 있다.

{% highlight python %}

class SpongeBob:
    pass

my_sponge_bob = SpongeBob()
print(type(my_sponge_bob)) # 출력 <class '__main__.SpongeBob'>
{% endhighlight %}

축하한다! 여러분은 방금 여러분만의 새로운 자료형을 정의했고, 그 자료형으로 부터
객체를 생성해 내었다!

참고로, **클래스로부터 객체를 만들어 내는 것을 인스턴스화(혹은 객체화) 라고 한다.**


## 클래스 변수 할당
어떤 캐릭터이든, 그 캐릭터를 스폰지밥이라고 부를 수 있으려면
우선 네모낳게 생겼고, 스폰지 이어야 하고, 네모 바지를 입어야 한다.
즉 다음의 공식이 성립한다.

"어떤 객체가 스폰지밥 자료형 이라면 반드시 그 객체는 네모낳고, 스폰지이고, 네모 바지라는 특성을 갖고 있어야 한다."
{: .text-center}


클래스 멤버변수를 설정하면 해당 클래스로 부터 생겨난 모든 객체는
해당 멤버변수를 갖고 태어난다.
무슨 말인지 모르겠다면 백문이 불여 일타다. 아래 코드를 작성해 보자.

클래스 멤버변수를 넣을 때에는 한 번 
들여쓰고 나서 평소에 변수를 할당하던 것 처럼 할당한다.

{% highlight python %}
class SpongeBob:
    figure = '네모 모양'
    pants = '네모 바지'
    is_sponge = True
    
my_sponge_bob = SpongeBob()

print(my_sponge_bob.figure)
print(my_sponge_bob.pants)
print(my_sponge_bob.is_sponge)

{% endhighlight %}

모든 스폰지밥은(스폰지밥, 그림밥, 파이썬밥) 모두 네모 모양이고, 네모 바지에, 넥타이를 입도록 정의했다.


## 멤버 접근 연산자 .

**my_sponge_bob.변수_이름** 의 . 은 '멤버 접근 연산자' 라고 부른다.
객체 안에 있는 특성에 접근할 수 있다.




