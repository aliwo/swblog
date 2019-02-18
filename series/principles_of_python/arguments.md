---
title:  "args와 kwargs" 
date:   2019-01-26 20:21:03 +0900
---

## Parameter 와 Argument

사실상 같은 것을 부르는 명칭인데,
* Parameter(파라미터) : **전달 받은** 변수를 메소드 안에서 부를 떄 쓰는 용어 
* Argument(인자) :  메소드를 호출 할 때 **전달할** 변수를 부를 때 쓰는 용어

으로 구분지어 놓으면 된다.



## 라떼에 들어가는 재료가 많아
이번 장에서는 메소드에 인자를 전달해 호출 할 때 사용할 수 있는
다양한 기법들을 소개한다. 

설명을 위해 인기 커피 프렌차이즈 스타북스로 들어가 보자.
스타북스는 커피에 다양한 옵션을 추가할 수 있어서 '나만의 커피'를 원하는 고객들에게
인기 만점이다. 
예를 들어 돌체 라때 클래스는 다음과 같이 다수의 인자를 받는다. 

{% highlight python %}

class DolceLatte:

    def __init__(self, shot, syrup, milk, ice, whip):
        self.shot = shot # 1 ~ 5 숫자 
        self.syrup = syrup # 1 ~ 5 숫자
        self.milk = milk # '일반', '저지방', '무지방', '두유'
        self.ice = ice # True 혹은 False
        self.whip = whip # True 혹은 False
    
{% endhighlight %}

그리고 다음과 같이 각 고객의 주문을 나타내는 튜플이 있고, 주문 튜플들의 리스트가 만들어져 있다고 하자.

{% highlight python %}
orders = [(2, 3, '두유', True, True), (4, 1, '저지방', False, False)] # 계속...
{% endhighlight %}

각 튜플들을 생성자에 넣어 DolceLatte 객체를 만들고 싶다. 여러분들이라면 어떻게 할 것인가?
일단 스스로 작성해 보도록 하자.


{% highlight python %}
class DolceLatte:

    def __init__(self, shot, syrup, milk, ice, whip):
        self.shot = shot # 1 ~ 5 숫자 
        self.syrup = syrup # 1 ~ 5 숫자
        self.milk = milk # '일반', '저지방', '무지방', '두유'
        self.ice = ice # True 혹은 False
        self.whip = whip # True 혹은 False


orders = [(2, 3, '두유', True, True), (4, 1, '저지방', False, False)] # 계속...

lattes = []
for order in orders:
    latte = DolceLatte(order[0], order[1], order[2], order[3], order[4])
    lattes.append(latte)

{% endhighlight %}

다 작성해 보았는가? 필자의 답안과 비교해보기를 바란다.

DolceLatte의 생성자에 각 인자를 전달하면서 불편함을 느낀 분들이 많았을 것이라고 생각한다.
order[0], order[1], order[2] 를 반복하고 있다.
문제는 순서대로 인덱스가 올라가는 방식임에도, 반복을 사용할 수 없다는 것이다. 



## * 연산자의 또다른 기능

**주의!!**       본 챕터에서 * 는 곱셈과는 전혀 상관이 없습니다.
{: .notice--info}

불편함을 느낀 여러분에게 DolceLatte 객체를 더 간편하게 만들 수 있는 방법을 소개한다.

{% highlight python %}
DolceLatte(*order) # DolceLatte(order[0], order[1], order[2], order[3], order[4])
{% endhighlight %}

그 방법은 시퀀스의 바로 앞에 * 를 붙이는 것이다.
`*<시퀀스>` 는 다음과 같은 의미를 지닌다.

"sequence 안의 각 요소를 순서대로 함수의 인자로 전달해라!" 
{: .text-center }


\* (에스터 리스크)를 사용할 때의 장점은 다음과 같다.
* 인자를 전달할 때 편하게 코드를 짤 수 있다.
* 나중에 order 튜플의 길이가 늘어나도 인자를 전달하는 부분은 코드를 수정할 필요가 없다.







## *args
이번엔 * args에 대해서 알아보겠다.
*args 의 의미는 다음과 같다.
 
"불특정 다수의 인자를 받겠다!"
{: .text-center }

인기 프랜차이즈 스타북스가 DolceLatte 의 옵션 개수를 늘렸다.
고객들은 새롭게 drizzle 과 cup 을 선택할 수 있게 되었다.

{% highlight python %}

class DolceLatte:

    def __init__(self, shot, syrup, milk, ice, whip, drizzle, cup):
        self.shot = shot # 1 ~ 5 숫자 
        self.syrup = syrup # 1 ~ 5 숫자
        self.milk = milk # '일반', '저지방', '무지방', '두유'
        self.ice = ice # True 혹은 False
        self.whip = whip # True 혹은 False
        self.drizzle = drizzle # '카라멜' 혹은 '초콜릿'
        self.cup = cup # '테이크 아웃' 혹은 '머그'
    
{% endhighlight %}
    


## **kwargs







