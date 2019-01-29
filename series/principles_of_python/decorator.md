---
title:  "함수를 꾸며주는 함수. 데코레이터"
date:   2019-01-28 20:21:03 +0900
---



## prerequisite
들어가기 전에 : 함수도 객체라는 것을 알고 있어야 한다.
-	함수도 객체(object)이다.
-	(객체 이므로) 변수에 함수를 할당할 수 있다. 이때, 변수() 로 해당 함수를 호출할 수 있다.
-	(객체 이므로) 멤버 변수를 가질 수 있다. func.__doc__ 등의 접근이 가능하다.
만약 위 내용이 뭔 소리인지 모르겠다면 파이썬 강의 ‘lambda 함수’ 편을 보고 옵시다.

또한 args 와 kwargs 의 활용방법도 알아야 한다.
만약 모른다면 이전 챕터들을 돌아보며 개념을 정리하고 돌아오도록 하자.


## 위험한 함수
파이썬 프로그래머인 당신은 평소처럼 출근해서 회사의 파이썬 서버에 
업데이트할 새로운 기능을 프로그래밍 하고 있었다. 그런데 상사로부터 메시지가 온다.

"저번 업데이트때 추가했던 함수가 이따금씩 원인 모를 에러를 일으키는 것 같아요. 
지금 고객 문의가 빗발치니까 원인 분석은 나중에 하기로 하고 일단은 try except 문으로 
감싸서 다른 코드는 문제없이 실행 될 수 있게 해주시겠어요?"
{: .text-center}


여러분은 바로 작업에 착수한다.

{% highlight python %}
import random

def random_true_or_false():
    return random.getrandbits(1)


def dangerous_func():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception

dangerous_func()
{% endhighlight %}

저번에 추가했던 dangerous_func 가 가끔씩 에러를 일으키는 상황이다. 
에러가 일어나도 무시하고 계속 코드를 실행할 수 있도록 새로운 함수 safe_func 를 만들도록 한다. 
그리고 dangerous_func 를 호출하는 문장을 주석처리하고 safe_func 호출로 대신한다.

{% highlight python %}
def safe_func():
    try:
        return dangerous_func()
    except Exception as e:
        print(e)

safe_func() # dangerous_func()
{% endhighlight %}


급한 불은 껐다. 방금은 문제가 되는 함수가 dangerous_func 하나여서 비교적 일이 간단했다. 
그러나 문제가 되는 함수가 더 많고, try except를 더 상세하게 만들어야 한다면 어떻게 될까?

{% highlight python %}
def dangerous_func1():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception


def dangerous_func2():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception


def dangerous_func3():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception

# dangerous_func 6 까지 있습니다.

def safe_func1():
    try:
        return dangerous_func1()
    except ValueError as e:
        print('Value Error 가 일어났습니다.')
        print(e)
    except AssertionError as e:
        print('AssertionError 가 일어났습니다.')
        print(e)
    except IndexError as e:
        print('IndexError 가 일어났습니다.')
        print(e)
    except Exception as e:
        print('알 수 없는 에러가 일어났습니다.')
        print(e)


# safe_func2, 3, 4 ... 6 까지 만들어야 할까?
{% endhighlight %}

문제를 해결하기 위해서 일일이 복사, 붙여넣기로 safe_func6 까지 만들어야 할까? 
그렇게 하면 문제를 해결할 수는 있지만, 똑같은 로직을 갖고 있는 safe_func 는 불어나기만 하고, 
새로운 dangerous_func가 더 발견되는 것이 점점 두려워 진다. 
만약 safe_func들을 일괄적으로 수정해야 하는 일이 생긴다면 일은 더 복잡해지고, 
수 많은 safe_func 를 수정하는 도중에 한 개라도 빼먹게 되는 사고는 상상하기도 싫어진다. 
악마를 물리치기 위해 더 큰 악마를 불러온다는 느낌이 들지 않는가?


## meet the decorator
결론부터 말하자면, 데코레이터를 사용하면 위 상황을 효과적으로 해결할 수 있다. 
먼저 완벽하게 해결한 코드를 제시하겠다. 읽어보고, 원리를 하나 하나씩 이해해 보도록 하자!

{% highlight python %}
def safe(dangerous_func):
    '''위험한 함수를 포장해서 안전한 함수로 만드는 데코레이터
    'safe' 를 소개합니다.'''
    def safe_func(): # 함수 safe 내부에서 함수 safe_func 를 정의합니다.
        try:
            return dangerous_func()
        except ValueError as e:
            print('Value Error 가 일어났습니다.')
            print(e)
        except AssertionError as e:
            print('AssertionError 가 일어났습니다.')
            print(e)
        except IndexError as e:
            print('IndexError 가 일어났습니다.')
            print(e)
        except Exception as e:
            print('알 수 없는 에러가 일어났습니다.')
            print(e)

    return safe_func # 정의한 safe_func 를 리턴합니다.


@safe # 데코레이터를 붙여주려면 @ 기호를 사용합니다. 
def dangerous_func1():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception


@safe
def dangerous_func2():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception

@safe
def dangerous_func3():
    print('warning warning!')
    if not random_true_or_false(): # 랜덤하게 에러 발생
        print('error occurred!')
        raise Exception



dangerous_func1()
dangerous_func2()
dangerous_func3()
print('안전하게 지났습니다!') # 항상 출력 됩니다.
{% endhighlight %}

실행해보면 dangerouse_func 에서 에러가 발생하더라도 항상 ‘안전하게 지났습니다’가 출력되는 것을 확인할 수 있다. 
데코레이터 safe가 제 역할을 다 했기 때문이다.


## decorator의 원리

{% highlight python %}
@decorator_a
def function_b():
    pass
{% endhighlight %}

를 했을 떄 내부적으로 일어나는 일은 다음과 같다.
* 함수 decorator_a 를 호출한다. 이떄 function_b 를 첫번째 인자로 전달한다.
* 호출 결과를 function_b 로 대체한다.

즉, function_b = decorator_a(function_b) 와 똑같다.
따라서 decorator_a 는 최소한 한 개의 인자를 받아야 하고, 
그 호출 결과로 함수 를 리턴해야 한다. 리턴할 함수는 데코레이터 안에서 내부 함수로 정의하는게 일반적이다.

{% highlight python %}
def decorator_a(func): # 인자를 받지않는 다면 에러가 발생한다.
    def inner_func(): # 내부 함수(inner function)를 정의한다.
        pass

    return inner_func # 정의한 내부 함수를 리턴한다.
{% endhighlight %}


그리고 내부 함수 안에서 인자로 전달받은 함수를 호출한다.
아래와 같이 기초적인 데코레이터의 형태가 만들어진다.

{% highlight python %}
def decorator_a(func):
    def inner_func():
        return func() # 인자로 전달받은 func 호출
    return inner_func

@decorator_a
def function_b():
    print('함수 b')
    pass

function_b()
{% endhighlight %}


이제 inner_func 안에서 func() 호출 전과 후에 실행할 코드를 작성할 수 있다.

{% highlight python %}
def decorator_a(func):
    def inner_func():
        print('함수를 곧 실행합니다.')
        return func() # 인자로 전달받은 func 호출
    return inner_func
{% endhighlight %}

func() 호출 후에 실행하고 싶은 코드가 있다면, 
먼저 func() 의 반환 값을 변수에 담아둘 필요가 있다.

{% highlight python %}
def decorator_a(func):
    def inner_func():
        print('함수를 곧 실행합니다.')
        result = func() # 인자로 전달받은 func 호출
        print('함수 실행을 성공적으로 마쳤습니다. 결과를 반환합니다.')
        return result
    return inner_func
{% endhighlight %}


## Wraps
데코레이터를 사용하면 겉으로 보았을 때는 기존의 함수 func를 ‘꾸민’ 것 처럼 보이지만, 
내부적으로는 전혀 다른 함수 inner_func를 호출하는 꼴이 된다.
여기서 문제가 되는 것은, 데코레이팅 과정 중에 func.__doc__ 과 같은 값을 잃어버린다는 것이다.

{% highlight python %}
def decorator_a(func):
    def inner_func():
        print('함수를 곧 실행합니다.')
        result = func() # 인자로 전달받은 func 호출
        print('함수 실행을 성공적으로 마쳤습니다. 결과를 반환합니다.')
        return result
    return inner_func

@decorator_a
def function_b():
    '''
    이 함수는 '함수 b' 라고 출력을 하는 함수입니다.
    '''
    print('함수 b')
    pass

print(function_b.\_\_doc\_\_) # None 출력. \_\_doc\_\_ 이 사라졌습니다.
{% endhighlight %}

이러한 손실을 막기 위해서 또다른 데코레이터 functools.wraps 를 사용한다.

{% highlight python %}
from functools import wraps

def decorator_a(func):
    @wraps(func)
    def inner_func():
        print('함수를 곧 실행합니다.')
        result = func() # 인자로 전달받은 func 호출
        print('함수 실행을 성공적으로 마쳤습니다. 결과를 반환합니다.')
        return result
    return inner_func

@decorator_a
def function_b():
    '''
    이 함수는 '함수 b' 라고 출력을 하는 함수입니다.
    '''
    print('함수 b')
    pass

print(function_b.\_\_doc\_\_) # '이 함수는 '함수 b' 라고 출력을 하는 함수입니다.' 출력.
{% endhighlight %}


## decorator 에 인자 전달
여태까지 아무런 인자를 받지 않는 함수를 꾸며왔습니다만, 인자가 있는 함수를 꾸밀때는 어떻게 해야 할까?





