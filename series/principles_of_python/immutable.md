---
title:  "mutable 과 immutable"
date:   2019-02-18 20:21:03 +0900
---


## 일 백번 고쳐죽어
예전에 튜플 자료형을 공부할 떄 튜플 자료형은 한 번 생성된 이후로
그 내용이 바뀌지 않는다고 배웠다. 임금에게 충성하는 충신 처럼
한 번 생성된 이후로 그 값을 바꾸지 않는 자료형을 immutable 한 자료형이라고 한다.
반대로 그 내용을 바꿀 수 있는 자료형을 mutable 한 자료형이라고 한다.


## 기본 자료형의 mutability

기본 자료형들의 mutable, immutable 여부는 다음과 같다.

| 클래스 | 유형 | mutability |
|:-------------:|:-------------:|:-----:|
| int | 정수 | immutable |
| float | 실수 | immutable |
| tuple | 튜플 | immutable |
| str | 문자열 | immutable |
| bool | 참, 거짓 | immutable |
| set | 집합 | mutable |
| list | 리스트 | mutable |
| dict | 딕셔너리 | mutable |




## mutable 한 값을 함수에 넣으면
다음 코드를 잘 살펴보자.
{% highlight python %}
def my_func(my_list):
    my_list.append(8)

numbers = [0, 1, 2] 
my_func(numbers) # mutable 한 객체인 리스트를 함수에 전달.
print(numbers) # [0, 1, 2, 8]
{% endhighlight %}

mutable 한 객체의 내용을 함수 내부에서 조작하면, 함수를 빠져나간 이후에도 변경사항이 남아 있는다.
단순 리스트의 조작은  

  
  







