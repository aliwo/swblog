---
title:  "변수의 스코프"
date:   2019-08-06 10:21:03 +0900
---

## 함수와 스코프

'함수' 챕터에서 다음 문제에 봉착했었다.
{% highlight python %}
kakao = 1000
sugar = 1000
milk = 1000

# 중략

def make_choco():
    kakao -= 60 # 함수안에서 전역변수를 수정하려고 시도한다. 에러!
    sugar -= 120
    milk -= 100
{% endhighlight %}

## 함수의 실행과 return

위 문제를 해결하기 위한 여러가지 방법이 있을 수 있지만 이번에는
`return`을 사용해서 문제를 해결해 보자.

키워드 `return` 은 함수 밖으로 값을 꺼내오고 함수 실행을 
종료하는 역할을 한다.

아래의 코드를 똑같이 작성한 후 직접 실행해보자.

{% highlight python %}

def return_3():
    return 3

print(return_3() + 7) # 10 출력.
{% endhighlight %}

함수의 이름 뒤에 `()` 괄호를 붙이는 것을 `함수를 호출한다.` 라고 한다.
이는 함수 안에 저장된 행동을 실행하는 것을 의미한다.

흔히 판타지 영화에서 마법사가 주문을 외우면 불덩이가 나가는것 처럼
주문을 외운다고 생각하면 이해하기 쉬울 것이다.

주문을 왼다. -> 마법이 발동한다 -> 불덩이 발사

함수를 호출한다. -> 함수가 실행된다. -> return 값을 반환한다.

함수를 호출하면 함수의 본문을 위에서 부터 아래로 실행해 나간다.
그러다가 return 을 만나면 실행을 중지하고 return 오른쪽의 값(혹은 변수)을 갖고
함수를 빠져나온다.

결과적으로 return_3() 이 3이 된다. 함수 return_3 이 3을 `반환`했다.
때문에 `print(return_3() + 7)` 은 `print(3 + 7)` 이 되고, 10을 출력하게 된다.


## make_choco 의 return

그렇다면 방금 배운 return 을 사용해서 아래와 같이 make_choco()
를 수정해 보자!

{% highlight python %}
kakao = 1000
sugar = 1000
milk = 1000

# 중략

def make_choco():
    return 60, 120, 100 # 필요한 재료의 양만 알려준다.
{% endhighlight %}

아쉽지만 make_choco() 안에서 재료의 양을 직접 줄이지는 못하고 
필요한 재료의 양만 알려주게 되었다. 
함수 안에서 재료를 직접 소모 시키는 방법은 나중에 같이 배울 것이다.

필요한 재료의 양만 알려 주는 함수가 되었으니
함수의 이름도 적절히 수정하겠다.

{% highlight python %}
kakao = 1000
sugar = 1000
milk = 1000

def choco_ingredients():
    return 60, 120, 100 # 필요한 재료의 양만 알려준다.
    
def milk_choco_ingredients():
    return 60, 120, 200
        
def dark_choco_ingredients():
    return 60, 120, 200
    
    
{% endhighlight %}

초코를 만들 때에는 다음과 같이 필요한 재료량을 
함수로 부터 가져온 뒤에, 총 재료양 에서 빼면 된다.

{% highlight python %}

# 초략

used_kakao, used_sugar, used_milk = choco_ingredients()
kakao -= used_kakao
sugar -= used_sugar
milk -= used_milk

{% endhighlight %}



