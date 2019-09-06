---
title:  "조건문"
date:   2019-08-20 11:21:03 +0900
---

## 초코함수의 결함
충격일지도 모르겠지만, 우리가 만든 초코 함수에는 심각한 결함이 하나 있다.
"사용하기 불편하다", "함수 안에서 재료를 감소시키지 못한다" 등의 작은 문제가 아니다.
아주 심각한 문제이다.

초코를 많이 만들어서 이제 재료가 떨어진 상황을 가정해 보자.

{% highlight python %}

kakao = 10 # 더 이상 재료가 없다!
sugar = 20
milk = 100

def choco_ingredients():
    return 60, 120, 100 # 필요한 재료의 양만 알려준다.
    
def milk_choco_ingredients():
    return 60, 120, 200
        
def dark_choco_ingredients():
    return 60, 120, 200
        
# 재료가 없는데 초코를 만든다?
k, s, m = choco_ingredients()
kakao -= k
sugar -= s
milk -= m

print(kakao) # -50
print(sugar) # -100
print(milk) # 0
{% endhighlight %}


## 재료가 음수가 된다고??
방금 우리가 만든 파이썬 프로그램에서 오병이어의 기적이 일어났다.
초코 재료가 없는 상황에서 초코가 만들어 진 것이다.

이는 프로그램 상에서만 나타나는 기적이다. 실제 공장에서 
생산 관리를 할 때 위 프로그램을 사용했다면
한창 생산 도중에 더 이상 초코가 나오지 않는 대형사고가 터졌을 것이다.

문제는 재료의 남은 양을 고려하지 않는 다는 점에 있다.

빨리 이 사태를 해결해 보자.

## 문제 파악하기
우리가 직면한 문제를 정리하자면 다음과 같다.
* 재료 값이 음수가 되면 안 된다.
* 재료가 부족한데도 초코가 만들어 진다. 

그렇다면 다음과 같은 해결방법을 생각해 볼 수 있다.
* 초코를 만들기 전에 재료가 충분한지 확인한다.

## 크고 작음을 비교하는 방법
재료가 충분한지를 확인하려면
`현재 재료양 - 사용할 량 >= 0` 인지를 확인하면 된다. 
파이썬에서 크고 작음을 비교하려면 <, >, <=, >= 연산자를 사용하면 된다.

{% highlight python %}
k, s, m = choco_ingredients()
if kakao - k < 0:
    print('카카오 부족')
if sugar - s < 0:
    print('설탕 부족')
if milk - m < 0:
    print('우유 부족')
{% endhighlight %}
우리는 위와 같은 방식으로 부족한 재료를 미리 알 수 있다.

그렇다면 재료가 충분할 때에만 재료를 감소시키고 초코를 만드려면 어떻게 할까?
3가지  조건을 묶으면 된다.



## 문제 해결

{% highlight python %}

kakao = 10  # 더 이상 재료가 없다!
sugar = 20
milk = 100


def choco_ingredients():
    return 60, 120, 100  # 필요한 재료의 양만 알려준다.


def milk_choco_ingredients():
    return 60, 120, 200


def dark_choco_ingredients():
    return 60, 120, 200


# 재료가 없는데 초코를 만든다?
k, s, m = choco_ingredients()
has_kakao = kakao - k < 0
has_sugar = sugar - s < 0
has_milk = milk - m < 0

if has_kakao:
    print('카카오 부족')
if has_sugar:
    print('설탕 부족')
if has_milk:
    print('우유 부족')

if has_kakao and has_sugar and has_milk:
    kakao -= k
    sugar -= s
    milk -= m

{% endhighlight %}

