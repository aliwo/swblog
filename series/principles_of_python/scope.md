---
title:  "변수의 스코프"
date:   2019-02-19 16:21:03 +0900
---

## 서울의 김씨와 부산의 김씨
문제를 하나 내겠다. 서울 특별시 강남구 개포동에 사는 김씨와 부산광역시 동래구 낙민동에 사는 김씨는
서로 같은 사람일까?

답은? 당연히 아니다. 성이 같다고 해서 같은 사람이 아니다. 같은 사람이라면 어떻게 서로 다른 지역에 공존하겠는가?
신도 아니고.

그럼 다시 문제를 내겠다.

아래의 파이썬 코드에서 function_1의 변수 a와 function_2 의 변수 a 는 같은 a 일까 ?
{% highlight python %}
def function_1(a):
    return a + 1

def function_2(a):
    return a + 2
{% endhighlight %}

아니다. 서로 다른 a 다. 이들은 이름이 같다는 것을 제외하면 연관이 없다.



## 이 구역의 a 는 나야
같은 이름의 변수일 지라도 scope 에 따라서 서로 다른 변수로 취급된다.
여기서 scope 가 무엇인지 짚고 넘어가도록 하자.

scope를 영어사전에서 찾아보면 다음과 같이 나온다.

"(관찰, 활동의)범위, 지역"
{: .text-center} 

변수는 선언되는 시점에서 해당 변수의 활동 영역(scope)이 정해진다. 함수 function_1() 안에서
만들어진 변수 a 의 경우 function_1()의 scope 안에 들어간다. 
함수 function_1() 밖에서는 a에 접근할 수 없으며, function_1() 이 종료되면 변수 a 도 삭제된다.

{% highlight python %}
def function_1(a):
    return a + 1 # a 는 function_1 scope 의 변수
    
function_1(3)
print(a) # 에러 발생! a 는 이미 삭제되었다.
{% endhighlight %}



## 구역에도 위아래가 있어
하위 스코프에서는 상위 스코프에 접근할 수가 있다.

{% highlight python %}
a = 3 # 모듈(파이썬 스크립트 파일) scope
def function_1():
    return a + 1 # 상위 scope 의 a 에 접근한다.
    
function_1()
print(a) # a는 모듈 scope 에서 정의되었으므로 함수 호출이 종료되어도 계속 살아남는다.
{% endhighlight %}

