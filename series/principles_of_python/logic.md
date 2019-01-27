---
title:  "논리 연산자"
date:   2019-01-26 20:21:03 +0900
---

## 참과 거짓
컴퓨터는 1과 0으로 되어 있다는 말을 들어본 적이 있는가? 1은 값이 있다는 것을 의미하고 
0은 값이 없다는 것을 의미한다. 이처럼 참과 거짓 두 가지 값으로 되어 있는
자료형을 bool 자료형이라고 한다.

## True or False
파이썬에서 '참' 은 대문자로 시작하는 True 로 표현하며, '거짓' 은 대문자로 시작하는 False 로 표현한다.
{% highlight python %}
my_true = True
my_false = False
{% endhighlight %}


## 라면을 끓일 수 있는가?
라면을 끓이는 데에는 어떤 재료들이 필요할까? 라면, 물, 냄비, 가스, 젓가락 정도를 생각해 볼 수 있다.
이 중 하나라도 없다면 뿌셔뿌셔로 만족하거나, 젓가락 없이 손으로 라면을 먹어야 하는 불상사가 발생할 것이다.
라면을 끓일 수 있는지 여부를 파이썬으로 표현해보자. 

어느 하나라도 False 라면 False 가 되는 연산자 and 를 사용하면 모든 재료가 True 인지 검사할 수 있다.
{% highlight python %}
# ramen.py

ramen = True
water = True
pot = True
gas = True
chopstick = True

print(ramen and water and pot and gas and chopstick) # True 출력

# 재료 중 어느 하나라도 False 가 되면 라면을 끓일 수 없다.
water = False # 물이 없다...
print(ramen and water and pot and gas and chopstick) # False 출력. 라면을 못 끓인다.

{% endhighlight %}


## 김치는 있어도 되고 없어도 된다.
취향 차이에 따라 다분히 의견이 갈릴 수 있는 이야기이지만 일단 라면을 먹는데 김치는 있어도 되고
없어도 된다고 치겠다. or 연산자는 둘 중 하나만 True 여도 True 를 리턴한다.
{% highlight python %}
ramen_available = True
kimchi = True

print(ramen_available or kimchi) # True 출력. 김치가 있으면 라면을 맛있게 먹을 수 있다.
kimchi = False
print(ramen_available or kimchi # True 출력. 김치가 없어도 먹을수는 있다.

{% endhighlight %}

## 다 끓인 라면을 엎었다면.
다 끓인 라면을 엎었을 경우, 라면을 더 이상 못 먹게 된다.
True 였던 값을 False 로 바꾸려면 not 연산자를 사용한다. 
not 연산자는 bool 값을 반전한다. (물론 False 였던 값을 True 로도 바꿀 수 있다.)

{% highlight python %}
ramen = True

print(not ramen) # False 출력. 라면을 못 먹게 되었다.

{% endhighlight %}


## 나는 진라면만 먹어
라면에도 종류가 있다. 신라면, 진라면, 너구리 등등.
진라면만 먹는 사람은 ramen 이 '진라면' 이어야만 라면을 먹을 수 있다고 하자.
변수의 값을 조사하려면 == 연산자를 사용한다. 비단 파이썬 뿐만 아니라 다른 언어에서도 
값을 비교하기 위해서 기호 == 을 사용하는데, = 은 할당 연산자로 이미 사용했기 때문에 할당 연산자와 구분하기 위해 ==
을 사용한다.
{% highlight python %}

ramen = '신라면'
print(ramen == '진라면') # False 출력. 진라면만 먹는 사람은 신라면은 안 먹는다.

ramen = '진라면'
print(ramen == '진라면') # True 출력. 드디어 진라면을 먹게 되었다.

{% endhighlight %}


## 논리연산자 정리
라면에 빗대어 설명한 논리 연산자들의 기능을 정리하자면 다음과 같다.

* and 연산자 : 모든 피연산자의 값이 True 라면 결과값이 True가 된다. 하나라도 False 라면 결과는 False 가 된다. 
* or 연산자 : 피연산자 중 하나라도 값이 True 이면 결과값은 True 이다. 모든 피연산자가 False 라면 결과는 False 이다.
* not 연산자 : bool 값을 반전한다. True 는 False 가 되고, False 는 True 가 된다.
* == 연산자 : == 양쪽 변수의 값이 일치하면 True, 불일치 하면 False 를 리턴한다.



## 짜파게티는 인정해주지
평생 빨간 라면만 먹고 살아야 한다면 삶이 너무 삭막하지 않은가. 진라면만 먹는 사람도
짜파게티 정도는 인정해 준다고 하자. ramen 이 '짜파게티' 혹은 '진라면' 이라면
라면을 먹을 수 있다.

라면을 먹을 수 있을지 판단하기 위해서는 목록 [짜파게티, 진라면] 중에 ramen 이 들어있는지를
확인해야 한다. 어떤 변수가 목록 중에 들어있는지를 조사하려면 in 연산자를 사용한다.

{% highlight python %}
eatable_ramen = ['진라면', '짜파게티']
ramen = '신라면'
print(ramen in eatable_ramen) # False 출력. 신라면은 못 먹는다.

ramen = '짜파게티'
print(ramen in eatable_ramen) # True 출력. 짜파게티는 먹어 주겠다.
{% endhighlight %}

in 연산자 : 목록(sequence 라고 한다.) 중에 특정 변수가 들어있는지를 조사한다.



