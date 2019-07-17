---
title:  "참과 거짓"
date:   2019-03-05 20:21:03 +0900
---

## 까다로운 손님

![image-center]({{ site.baseurl }}/assets/images/2019-07-17-choco.jpg){: .align-center}

초코 공장의 매장에 까다로운 손님이 한 명 왔다.
이 손님은 초코에 200g 이상의 설탕이 들어있지 않다면
'맛 없다' 라고 불평한다.

이 손님이 초코를 맛있다고 느끼는지, 맛 없다고 느끼는지 확인해 보는
파이썬 프로그램을 만들어보자.


## 비교
초코에 설탕이 200g 이상 들어 있으면 손님은 '맛있다' 라고 느낄 것이다.

수학시간에 크고 작음을 비교 할 때에는 기호 `>` 와 `<` 를 사용했다.
파이썬에서도 똑같다.
{% highlight python %}
>>> sugar = 300
>>> sugar > 200
True # 맛있어!
{% endhighlight %}

`>` 와 `<` 는 초과와 미만을 검사하는데 사용되고,
`<=` 와 `>=` 는 이상과 이하를 검사하는데 사용된다. 

{% highlight python %}
>>> sugar = 200
>>> sugar >= 200
True
>>> sugar <= 200
True
{% endhighlight %}

설탕이 200g 보다 적다면, 손님은 맛없다고 생각할 것이다.

{% highlight python %}
>>> sugar = 100
>>> sugar >= 200
False # 우웩
{% endhighlight %}

## True 와 False
연산의 결과로 나오는 True 와 False 는 어떤 자료형일까?
True 와 False 는 참과 거짓을 나타내는 boolean 자료형 이라고 한다.
줄여서 bool 이라고 한다.

{% highlight python %}
>>> type(True)
<class 'bool'>
{% endhighlight %}

## 설탕만 준다면?
설탕만 검사하는 파이썬 프로그램이라면 초코가 아니라
설탕만 200g 이 들어간 설탕물을 주어도 결과가 True 가 되어 버리게 된다.

{% highlight python %}
>>> sugar >= 200
True
{% endhighlight %}

하지만 그건 우리가 원하는 바가 아니다.
그럼 카카오가 들어 있는지, 우유도 들어 있는지를 `함께` 검사하려면 어떻게 해야 할까?

{% highlight python %}
>>> sugar = 300
>>> kakao = True
>>> milk = True
>>> sugar >= 200 and kakao and milk 
True
{% endhighlight %}

kakao 와 milk 변수에 각각 bool 값 True 를 할당했다.
그리고 and 연산을 사용해 설탕의 양과 카카오와 우유를 `함께` 검사했다.
이처럼 어떤 조건을 함께 검사하고 싶다면 and 를 사용한다.

and 가 들어간 계산식은 and 왼편과 오른편의 값이 모두 True 일 때만
계산식의 답이 True 가 된다는 걸 기억하자.

## 초코를 만들 수 있을까?
까다로운 손님은 설탕물도, 쓴 초콜릿도 아닌 달달한 초콜릿을 받아 들고
만족스럽게 돌아갔다.

그건 그렇고, 도중에 and 를 배웠으니 or 도 배워보자.
almond_milk 는 초코를 만드는 데에 있어도 되고 없어도 된다.
milk 가 없을때 대신 almond_milk 를 사용할 수 있다고 하자.
즉, milk 혹은 almond_milk 둘 중 하나는 꼭 있어야 초코를 만들 수 있다.

{% highlight python %}
>>> sugar = True
>>> kakao = True
>>> milk = True
>>> almond_milk = False
>>> sugar and kakao and (milk or almond_milk) # almond_milk 는 있어도 되고 없어도 되!
True # 초코를 만들 수 있다.
{% endhighlight %}

or 는 or 양 쪽에 하나라도 True 인 조건이 있다면 그 결과가 True 가 된다.
반대로, 양 쪽 다 False 라면 그 결과는 False 가 된다. 
만약 우유도 없고 아몬드유도 없다면 어떻게 될까?

{% highlight python %}
>>> sugar = True
>>> kakao = True
>>> milk = False # 우유가 없네!
>>> almond_milk = False # 아몬드유도 없다!
>>> sugar and kakao and (milk or almond_milk)
False # 초콜렛 실패!
{% endhighlight %}

계산식에서 사용된 () 괄호는, 수학시간에 배웠던 괄호와 똑같은 용도다.
괄호 안의 계산식을 먼저 계산한다.
{: .text-center}
{: .notice--info}

## 뒤집기
not 을 사용하면 bool 값을 뒤집을 수 있다.
직관적이니, 따로 설명은 하지 않겠다.
{% highlight python %}
>>> not True
False
>>> not False
True
{% endhighlight %}



## 정리하기
* 크고 작음을 비교할 때는 <, >, <=, >=
* 같이 비교하고 싶을 때에는 and, or
* bool 값을 뒤집을 때에는 not

