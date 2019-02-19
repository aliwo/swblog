---
title:  "args와 kwargs" 
date:   2019-01-26 20:21:03 +0900
---

## Parameter 와 Argument

사실상 같은 것을 부르는 명칭인데,
* Parameter(파라미터) : **전달 받은** 변수를 메소드 안에서 부를 떄 쓰는 용어 
* Argument(인자) :  메소드를 호출 할 때 **전달할** 변수를 부를 때 쓰는 용어

으로 구분지어 놓으면 된다.


## Positional Argument 와 Keyword Argument

Argument 는 다시 두 종류로 나뉜다.

{% highlight python %}

def my_func(a, b, c): # positional arguments
    pass

def my_func2(a=1, b=2, c=3): # keyword arguments
    pass

def my_func3(a, b=2):
    pass

def my_func4(a=1, b): # 에러!!
    pass

{% endhighlight %}


positional argument 의 특징은 다음과 같다.
* 반드시 인자를 전달해야 한다. 만약 positional argument 의 자리를 비워두고 함수를 호출하면 에러가 난다.



keyword argument 의 특징은 다음과 같다.
* 이름으로 호출할 수 있다. (물론 이름으로 호출하지 않아도 되나, 이름으로 호출하는 것을 권장한다.)
* 기본 값을 갖는다.
* positional argument 가 모두 정의된 후에 정의한다. (my_func4) 를 보기


{: .notice--info}
**keyword argument 가 반드시 positional argument 뒤에 와야 하는 이유**       
예를 들어 my_func4 를 호출할 때
```python
my_func('hi')
```
일때, 'hi' 가 a에 할당된 것인지, 혹은 a 는 기본값을 사용하고 b에 'hi' 를 할당한 것인지
구분할 수 없게 된다.


## 라떼에 들어가는 재료가 많아
이번 장에서는 메소드에 인자를 전달해 호출 할 때 사용할 수 있는
다양한 기법들을 소개한다. 

설명을 위해 인기 커피 프렌차이즈 스타북스로 들어가 보자.
스타북스는 커피에 다양한 옵션을 추가할 수 있어서 '나만의 커피'를 원하는 고객들에게
인기 만점인 커피 프렌차이즈다. 
예를 들어 스타북스의 메뉴 돌체 라때는 생성자에서 다음과 같이 다수의 인자를 받는다. 

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

각 튜플들의 각 요소들을 순서대로 생성자에 전달해
DolceLatte 객체를 만들고 싶다. 여러분들이라면 어떻게 할 것인가?
일단 DolceLatte 객체를 인스턴스화 하는 코드를 스스로 작성해 보도록 하자.


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
문제는 순서대로 인덱스가 올라가는 방식임에도, for 문 같은 반복을 사용할 수 없다는 것이다. 



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
최근 모 유명 스트리머가 견과류를 커피에 뿌려서 맛있게 먹는 방송이 대 유행함에 따라
견과류 토핑을 찾는 사람들이 늘어났다.
이에 부응해 스타북스는 돌체 라떼에 견과류 토핑을 추가할 수 있도록 업데이트 하려고 한다.


그러나 기존에 DolceLatte 를 주문할 때에도 이미 물어보는 옵션의 종류가 많기 때문에, 
(샷, 시럽, 우유, 얼음, 휘핑... 5개) 주문할 떄 직원이 묻는 것이 아닌, 특별히 견과류를 요청하는
사람에게만 견과류 토핑을 제공하려고 한다.

즉 기존에 5개의 인자를 전달해 DolceLatte 를 생성하는 코드는 그대로 두고 싶다.
대신 5개의 인자 이후에 견과류 인자를 추가로 전달받았을 때에만 견과류 토핑을 추가하려고 한다.
디폴트 값을 갖는 keyword argument 를 사용해서 구현할 수도 있지만, 이번에는 *args 를 
사용해서 구현해 보도록 하겠다.

*args 의 의미는 다음과 같다.
 
"불특정 다수의 인자를 받겠다!"
{: .text-center }

{% highlight python %}

class DolceLatte:

    def __init__(self, shot, syrup, milk, ice, whip, *args):
        self.shot = shot # 1 ~ 5 숫자
        self.syrup = syrup # 1 ~ 5 숫자
        self.milk = milk # '일반', '저지방', '무지방', '두유'
        self.ice = ice # True 혹은 False
        self.whip = whip # True 혹은 False

        self.almond = args.count('아몬드')
        self.cashnut = args.count('캐슈넛')
        self.walnut = args.count('호두')

nut_dolce_latte = DolceLatte(4, 1, '저지방', False, False, '아몬드', '아몬드', '호두')
    
{% endhighlight %}

5개의 인자 이후에 *(에스터리스크) 를 사용해서 특별한 인자 args를 정의했다.
args 는 메소드 안에서 사용할 수 있는 튜플이 되며, whip 이후의 모든 positional argurment 는 전부
이 튜플 안으로 들어가게 된다. 
개수가 정해져 있지 않기 때문에 이를 '가변 인자'
<a href="https://docs.python.org/dev/tutorial/controlflow.html#arbitrary-argument-lists" target="_blank">(Arbitrary Argument Lists)</a> 
라고 부른다. 

위 코드에서는 '아몬드', '아몬드', '호두' 인자가 모두 args 라는 이름의 튜플에 들어갔다.

*를 붙이면 가변인자가 되며, 이름은 꼭 args일 필요는 없다. 하지만 args 라고 붙여주는 것이 관례(Convention) 이므로
반드시 다른 이름을 써야할 특별할 이유가 없다면 args 라고 이름 짓도록 하자. 


## **kwargs







