---
title:  "리스트"
date:   2019-01-19 20:21:03 +0900
---


## 자동판매기 

{% highlight python %}
# 자판기의 음료수 목록
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']
{% endhighlight %}

우리는 이미 리스트 자료형을 사용해 본 적이 있다.
자판기의 음료수 목록을 표현하기 위해서 음료수 이름들을 줄줄이 나열했던 것을 기억하는가?

**입력과 출력** 장에서 보왔던 이 자동판매기 음료수 목록이 바로 리스트이다.


## 리스트
리스트는 가장 기본적인 ‘순서가 있는 자료형’ 이다. 

파이썬 리스트의 특징은 다음과 같다.
* 요소 간에 순서가 있다.
* 요소의 순서는 0번째 부터 시작한다. (즉 위 리스트에서는 파워에이드가 0번째 음료수가 된다.)
* 고의로 바꾸지 않는 한 요소(item)의 순서가 유지된다.
* 선언 이후에 요소를 추가하거나 제거할 수 있으며, 이에 따라 요소의 순서가 변동될 수 있다.
* mutable(변할 수 있는) 한 자료형이다. mutable 이 무엇인지에 대해선 <a href="{{ site.baseurl }}/series/principles_of_python/arguments" target="_blank">
'mutable 과 immutable'</a>시간에 배우도록 하자.
* 서로 다른 자료형도 하나의 리스트 안에 들어갈 수 있다. 따라서 하나의 리스트 안에 정수도, 문자열도, 실수도 다 같이 들어갈 수 있다.
(이는 자바의‘배열’과 구분되는 차이이다. 자바의 배열은 같은 자료형만 들어간다.)


## 리스트의 선언
리스트는 [] 을 사용해서 선언할 수 있다.
{% highlight python %}
my_list = [] # 빈 리스트 생성
{% endhighlight %}

list() 도 빈 리스트를 생성한다. 지금은 그냥 `[]` 와 `list()` 중 
마음에 드는 방법을 사용하면 된다.
{% highlight python %}
my_list = list() # 빈 리스트 생성
{% endhighlight %}

그리고 그 안에 여러가지 객체를 담을 수 있다. 서로 자료형이 달라도 담을 수 있다.
{% highlight python %}
my_list = [3, 2.0, '안녕'] 
{% endhighlight %}


## 리스트에 새로운 요소 추가하기 

우리가 만들었던 파이썬 자동판매기가 선풍적인 인기를
끌고 있다고 한다. 자동 판매기 회사 사장으로 부터 
자판기에 새로운 음료수를 추가해 달라는 요청이 왔다.

![image-center]({{ site.baseurl }}/assets/images/2019-03-03-ceo.jpg){: .align-center}

**우리 자동판매기에 새로운 음료수를 들여 놓고 싶어요!**
{: .text-center}

이렇게 귀여운 사장의 부탁을 들어주지 않을 수 없다. 리스트에 새로운 요소를 추가하고 싶다면 .append() 를 사용하면 된다. 
{% highlight python %}
# 자판기의 음료수 목록
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

merchandise.append('데자와')
merchandise.append('마운틴듀')

print(merchandise)

{% endhighlight %}

이러면 사장님도 행복해 하실 것이다.
우리는 내친 김에 리스트가 갖고 있는 다른 기능들도 살펴보도록 하자.


## 리스트 요소에 접근
리스트는 0번 부터 번호를 매겨서 요소를 순서대로 저장한다.
자판기의 음료수 목록 중 n 번째 요소에 접근하고 싶다면 다음과 같이 한다. 

{% highlight python %}
# 자판기의 음료수 목록
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

print(merchandise[0]) # merchandise 리스트의 0 번째 요소, 파워에이드
print(merchandise[1]) # merchandise 리스트의 1 번째 요소, 코카콜라
print(merchandise[6]) # merchandise 리스트의 6 번째 요소, 핫식스

{% endhighlight %}

리스트 각 요소에 매겨진 순서를 인덱스`index` 라고 부른다.


## ()뒤에서 부터) 리스트 요소에 접근
뒤에서 부터 리스트 요소에 접근할 수도 있다. 인덱스가 각각
* -1 일때, 맨 뒤에서 첫 번째 요소에 접근한다.
* -2 일때 맨 뒤에서 두 번째 요소에 접근한다.

{% highlight python %}
# 자판기의 음료수 목록
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

print(merchandise[-1]) # merchandise 리스트의 뒤에서 첫 번째 요소, 핫식스
print(merchandise[-2]) # merchandise 리스트의 뒤에서 두 번째 요소, 스프라이트

{% endhighlight %}

인덱스가 음수일 때는 0부터 세는 것이 아니라 -1 부터 세는데,
이는 숫자 0에 +0 혹은 -0 이 없기 때문이니 이해해주도록 하자.



## 리스트 요소의 탐색 

for 문을 사용해서 리스트의 요소를 




## 리스트 슬라이싱


## 연습 문제

<a href="https://py.checkio.org/en/mission/sort-array-by-element-frequency/" target="_blank">링크</a>













