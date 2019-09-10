---
title:  "객체와 클래스"
date:   2019-09-06 11:21:03 +0900
---

## 달콤한 초콜릿

![image-center]({{ site.baseurl }}/assets/images/2019-09-09-choco.jpg){: .align-center}

달콤한 초콜릿을 생각해 보자. 어떤 것들이 떠오를까?
* 달콤한 맛 (느므조아)
* 만지면 끈적거림
* 약간 딱딱하지만 쉽게 부러짐
* 제조일자
* 유통기한
* 가격

이러한 특징들을 프로그램 안으로 옮겨올 수는 없을까?

여태까지 우리는 정수, 문자열 등의 값들을 저장하고 활용해 보았다.
정수 값은 int 자료형으로 표현해 보았고 문자열 값은 str 자료형으로 표현해 보았다.

우리가 정수와 문자열을 사용해 왔던 것 처럼
이제는 '초콜릿'을 우리가 직접 정의해서 프로그램 안에서 사용해 볼 것이다.
아래 코드를 따라서 똑같이 작성해 보자.

{% highlight python %}

class Choco:
    sweetness = 5 # 5점 만점에 5점의 달콤함.

print(Choco.sweetness) # 5 출력

{% endhighlight %}

키워드 `class` 는 새로운 자료형을 정의한다. 우리가 사용했던 int, str
처럼, 이제는 Choco 라는 자료형이 생긴 것이다. 

이 안에 변수를 만들면
`class이름.변수이름`으로 클래스 안의 변수에 접근할 수 있다.
이때 `.` 을 점 연산자(dot operator) 라고도 부른다.
이처럼 클래스 안에 들어있는 변수를 `멤버변수` 라고 한다. 

멤버변수는 클래스의 특징(속성, attribute)을 나타낸다. 
앞서 초콜릿을 생각하면서 달콤함, 딱딱함 등을 떠올려 본 것 처럼
초콜릿에는 '달콤함' 이라는 속성이 있으니 이를 `sweetness = 5` 로 표현한 것이다. 


## 객체와 클래스
방금 만들어본 클래스는 사실 초콜릿 이라기 보다는 초콜릿을 만드는 '틀'에
가깝다. (혹은 초콜릿 레시피, 초콜릿 설계도라고 할 수도 있다.)

초콜릿 틀을 가지고 있으면 그 안에 여러가지 재료를 넣어서 초콜릿을 많이 만들 수 있듯이
우리가 정의한 초콜릿 클래스를 사용해서 계속해서 초콜릿 객체를 만들 수 있다.

다음과 같이 코드를 살짝 바꿔보자.

{% highlight python %}
class Choco:

    def __init__(self, sweetness):
        self.sweetness = sweetness

print(Choco(5).sweetness) # 5 출력
{% endhighlight %}

먼저, Choco 클래스를 이용해서 Choco 객체를 만드는 방법은 `Choco()` 이다.
함수를 호출할 때 처럼 () 괄호를 붙이면 된다.

함수를 호출 할 때 처럼 괄호 안에 변수를 넣을 수 있다. 위 코드에서는
`Choco(5)` 라고 하였다.

클래스로부터 객체를 만드는 것을 `인스턴스화` 라고 한다. (객체를 인스턴스라고도 부른다.) 
인스턴스화 할 때에는 특별한 이름의 함수인 `__init__` 이 호출된다.

클래스 안에 들어 있는 변수를 `멤버변수` 라고 불렀던 것 처럼 클래스 안에 들어 있는
함수를 `메소드(method)` 라고 부른다. 메소드에는 특별한 규칙이 있다.

## \_\_init\_\_ 과 self

{% highlight python %}

def __init__(self, sweetness):
    self.sweetness = sweetness

{% endhighlight %}
파이썬에서 메소드의 첫번째 인자는 반드시 self 이며, 이는 바깥에서 전달해줄 필요가 없이
자동으로 할당된다. 따라서 호출할 때에는 self 를 제외한 나머지 인자만 전달해 주면 된다.
즉 `Choco(5)` 에서 5는 sweetness 에 할당된다.

위 \_\_init\_\_ 메소드가 하는 일은 한 가지이다. `self.sweetness = sweetness` 이다.
여기서 self 는 '자기 자신' 을 가리킨다. 즉, 지금 생성된 Choco 객체를 가리킨다. 
방금 막 생성된 Choco 객체 안에 sweetness 라는 이름의
변수를 집어 넣는 것이다. 그 값은 \_\_init\_\_ 메소드에 전달된 sweetness 이다. 즉, 5가 할당된다.

결과적으로 Choco(5) 는 `sweetness 5` 를 가진 초코 객체가 되고, 다음과 같이
Choco(5).sweetness 로 접근 할 수 있다.

{% highlight python %}
print(Choco(5).sweetness) # 5
choco = Choco(5) # 생성된 객체를 변수에 할당
print(choco.sweetness) # 똑같이 5 출력
{% endhighlight %}

여러가지 당도의 초콜릿을 만들 수 있다.

{% highlight python %}
choco1 = Choco(6) # 단 초코
choco2 = Choco(5) # 초코
choco3 = Choco(1) # 쓴 초코

print(choco1.sweetness)
print(choco3.sweetness)
{% endhighlight %}


## 정리하기

우리는 다음과 같이 초코 클래스를 만들어 보았다.

{% highlight python %}

class Choco:

    def __init__(self, sweetness):
        self.sweetness = sweetness

{% endhighlight %}

그리고 다음의 사실을 배웠다.

* 새로운 자료형은 `class` 키워드를 사용해서 만든다.
* 메소드의 첫번째 인자는 항상 self 이며, 자동으로 할당되기 때문에 밖에서 전달해줄 필요가 없다.
* \_\_init\_\_ 은 클래스로부터 객체가 만들어질 때 호출되며, '생성자' 라고 부른다.

## 참고하기
\_\_init\_\_ 처럼
이름 양쪽에 \_\_ 가 달려있는 메소드들을 `Magic Method` 라고 한다.
이는 파이썬에서 특별한 목적을 갖고 사용하는 메소드 들로,
여러분들이 이름을 지을 때에는 이를 따라해서는 안 된다.








