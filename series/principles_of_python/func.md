---
title:  "함수"
date:   2019-01-26 20:21:03 +0900
---



## 프로그래밍의 함수

중학교 시절에 배웠던 수학의 함수를 떠올려 보자.
모눈 종이에 y = x 나 y = x + 7 등의 함수를 그렸던 것이 기억나는가? 
<br><br>
y = 2x 라는 함수가 있을떄
x가 각각 1, 2, 3 으로 주어졌다고 하자. y 값은 어떻게 될까?
y는 x에 2를 곱한 값이므로 각각 2, 4, 6 이 될 것이다.
우리는 입력 값 x 를 넣고 함수 식을 계산했을 때 결과 값 y를 구할 수 있다.

프로그래밍의 함수도 같은 원리로 동작한다. 입력값을 넣고 함수를 작동시키면
결과 값을 얻는다. 이 때 함수를 작동시키는 것을 '함수를 호출한다' 라고 한다.
프로그래밍에서 말하는 함수의 정의는 다음과 같다.

"함수는 입력을 받았을 때 결과 값을 내어 놓는 일련의 과정이다." 
{: .text-center}

## 함수의 호출
함수 이름 오른쪽에 () 괄호가 있다면 함수를 호출한다는 뜻이다.
이때 괄호 안에 함수의 입력으로 들어갈 값을 집어넣을 수 있다.
여태까지 우리는 여러번 함수를 호출해 왔다.
{% highlight python %}
print('learning python is so fun!')
{% endhighlight %}

우리가 흔히 사용하던 print('문자열') 라는 문장은 다음과 같은 의미이다.

"함수 print를 호출하겠다. 그 입력으로 '문자열' 이라는 문자를 집어넣는다."
{: .text-center}

## print 함수의 결과값 
결과값이 없는 함수도 있다.(사실 많다.)
print 함수는 대표적인 '결과값을 내어놓지 않는 함수' 이다. 
결과값으로 아무것도 내어 놓지는 않지만, 화면에 문자열을 출력하는 일을 한다. 
``` markdown
learning python is so fun!
```


## 함수 정의하기
여러분도 새로운 함수를 만들어 낼 수 있다. 이를 '함수를 정의한다' 라고 한다.
함수를 정의할때는 키워드 **def** 를 사용한다. 이는 '정의한다' 라는 뜻을 가진 영단어 define의 약자이다.
시험 삼아 y=2x를 파이썬의 함수로 만들어 보겠다.

{% highlight python %}
def my_function(x):
    return 2*x
{% endhighlight %}
my_function 은 함수의 이름이다. 
def 를 사용해서 함수를 정의할 때에는 반드시 함수의 이름을 지어주어야 한다.
함수의 이름을 지어줄 때에는 변수 이름을 지을 때와 
똑같은 규칙을 적용하면 된다. 영어 소문자를 사용하며, 띄어쓰기는 _ (언더스코어) 로 대신한다.
더하는 함수엔 add, 삭제하는 함수엔 delete 등 함수의 기능을 명확하게 설명해주는 이름이 좋은 이름이다.

함수를 정의할때 붙는 소괄호()는 함수에 들어갈 입력을 의미한다. 
(x) 는 하나의 입력을 받으며, 그 입력을 x 라는 변수에 할당하겠다는 의미이다.
입력을 받지 않는 함수의 경우에도 파이썬 문법상 소괄호는 반드시 붙여주어야 한다.

{% highlight python %}
def my_function(): # 입력을 받지 않는 함수
    return 10
{% endhighlight %}

입력을 여러 개 받을 때에는 ,(콤마) 로 구분한다.

{% highlight python %}
def add(a, b): # 입력을 두 개 받는 함수
    return a + b
{% endhighlight %}


함수의 구조를 정리하면 다음과 같다.
{% highlight python %}
def name(input): # name 은 함수 이름, input 은 입력 값
    # <코드 블럭>
{% endhighlight %}


## return

return 은 함수가 계산하는 결과 값을 의미한다. 
return 2*x 는 입력 x 에 2를 곱한 값을 결과 값으로 한다는 의미이다.
결과 값을 만들어 내는 것을 '결과를 리턴한다' 라고 한다.

{% highlight python %}
def my_function(x):
    return 2*x # x에 2를 곱한 값을 리턴한다.
{% endhighlight %}

return 은 함수 블럭 안에서 있어도 되고 없어도 된다. 만약 return 이 없는 경우
파이썬은 자동으로 return None 으로 인식한다. 
None 값을 리턴하는 함수 == 결과값을 리턴하지 않은 함수 이다. 

## return 값으로 변수 할당하기
{% highlight python %}
my_number = input()
{% endhighlight %}
input() 함수는 이미 여러분에게 익숙할 것이다. input 함수는 사용자가 터미널에 입력한 값을
결과값으로 리턴한다. input() 함수의 결과값을 변수에 할당하던 것 처럼, 여러분의 만든 함수의
결과값도 변수에 할당할 수 있다.

{% highlight python %}
def get_number_7():
    return 7

my_number = get_number_7()
print(my_number) # 7 출력
{% endhighlight %}

## 연습문제
가위바위보 프로그램을 개선해 보자.
플레이어1과 플레이어2가 낸 가위바위보 값을 입력받아
승자를 리턴하는 함수 eval_winner() 를 만들어서 호출하자.










