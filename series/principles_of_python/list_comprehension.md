---
title:  "리스트 컴프리헨션"
date:   2019-03-01 10:21:03 +0900
---

파이썬 콘솔을 열고 다음을 타이핑해보자.
{% highlight python %}
>>> [x for x in range(0, 10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
{% endhighlight %}

실행의 결과로 0 에서 9 까지의 정수가 담긴 리스트가 나왔다.
무슨 일이 일어난 것일까?


## 리스트 컴프리헨션이란
list comprehension : 파이썬이 제공하는 리스트를 만들기 위한 '간결' 하고도 '강력'한 방법이다.


## 사용법

for 문을 작성하는 것과 비슷한데, 대신 콜론`:`이 없고 양 끝을 [] 중괄호가 둘러 싸고 있는 모양이다.
{% highlight python %}
>>> [i for i in range(10)]
{% endhighlight %}

## 리스트 컴프리헨션과 if

if 문을 함께 사용할 수 있다. 다음은
0 부터 19 까지의 정수 중, 짝수 만 리스트에 담는다.
{% highlight python %}
>>>  [i for i in range(20) if i%2 == 0]
{% endhighlight %}



## 중첩
2 개의 리스트 컴프리헨션을 중첩해서 사용할 수도 있다.

{% highlight python %}
nums = [1, 2, 3, 4]
fruit = ["Apples", "Peaches", "Pears", "Bananas"]
print([(i, f) for i in nums for f in fruit])
# 출력 결과
# [(1, 'Apples'), (1, 'Peaches'), (1, 'Pears'), (1, 'Bananas'), 
# (2, 'Apples'), (2, 'Peaches'), (2, 'Pears'), (2, 'Bananas'), 
# (3, 'Apples'), (3, 'Peaches'), (3, 'Pears'), (3, 'Bananas'), 
# (4, 'Apples'), (4, 'Peaches'), (4, 'Pears'), (4, 'Bananas')]
{% endhighlight %}

다음 2중 for 문의 result 와 같은 내용을 만들어 낸다.
{% highlight python %}

result = []
nums = [1, 2, 3, 4]
fruit = ["Apples", "Peaches", "Pears", "Bananas"]

for i in nums:
    for f in fruit:
        result.append((i, f))

{% endhighlight %}



## 참고

<a href="https://mingrammer.com/introduce-comprehension-of-python/" target="_blank"> Comprehension 정리</a>

<a href="https://www.python.org/dev/peps/pep-0202/" target="_blank">PEP202</a>
