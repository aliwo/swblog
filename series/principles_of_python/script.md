---
title:  "스크립트와 입출력"
date:   2019-08-04 20:21:03 +0900
---

## 스크립트
초콜릿을 좀 더 본격적으로 만드려면, 레시피를 어딘가에 적어두는 것이 편하다.
매 번 초콜릿을 만들 때 마다 다음과 같이 인터프리터에 레시피를 붙여 넣어서는 
시간이 너무 오래 걸려서 납품 기한도 맞추지 못할 것이다.

{% highlight python %}
>>> sugar = 120
>>> milk_choco = 60 + sugar + 200
{% endhighlight %}

그래서 이제부터는 확장자 명이 .py 인 파일 안에 레시피를 적어두려고 한다.
.py 파일을 `파이썬 스크립트` 라고 부른다.

파이참 왼쪽의 `Project` 패널을 열어서, 폴더를 우클릭 -> New -> Python File 선택 -> 이름을 factory.py
라고 지어주자.

![image-center]({{ site.baseurl }}/assets/images/2019-08-04-script-01.jpg){: .align-center}

그리고 파일의 내용을 다음과 같이 적어준다.

{% highlight python %}
# 이곳은 초코 공장입니다.

sugar = 120
choco = 60 + sugar + 100
milk_choco = 60 + sugar + 200
dark_choco = 90 + sugar + 100
choco
milk_choco
dark_choco
{% endhighlight %}

파이썬 스크립트 안에서는 `>>>` 기호는 필요가 없다.
그리고 Ctrl + Shift + F10 을 누르면 실행 된다. (Alt + Shift + F10 인 경우도 있다.)


## 스크립트의 실행결과
실행 결과로는? 아래와 같은 메세지 하나가 나오고 끝났을 것이다.
```
Process finished with exit code 0
```
위 문구는 파이썬 코드가 잘 끝났음을 의미한다. 앞으로는 언급하지 않을 것이다.

## 출력

스크립트를 실행 할 때에는, 단순히 변수의 이름을 적어주는 것 만으로는,
그 안의 값이 출력되지 않는다. 출력하려면 print() 라는 것을 사용해야 한다.
다음과 같이 `factory.py` 를 새로 작성해 보자.

{% highlight python %}
# 이곳은 초코 공장입니다.

sugar = 120
choco = 60 + sugar + 100
milk_choco = 60 + sugar + 200
dark_choco = 90 + sugar + 100
print(choco)
print(milk_choco)
print(dark_choco)
{% endhighlight %}

그 출력 결과는 다음과 같다.
```
280
380
310
```

## 입력
출력의 반대로, 입력이라는 것도 있다. 단순한 입력으로는, 키보드로 
작성한 글을 파이썬 프로그램 안으로 집어넣는 것이 있는데, 이때는
`input()` 을 사용한다.

다음과 같이 내용을 수정해 보자.

{% highlight python %}
... 초략
sugar = int(input())
... 후략
{% endhighlight %}

실행을 해보면 바로 초콜릿의 무게가 출력되는 대신, 빈 화면에서 멈춰 있을 것이다.
빈 화면에 마우스를 클릭한 후 100 이라는 숫자를 적어주자. 그리고 엔터를 친다.
그러면 화면에 다음과 같이 출력될 것이다.

```
100 # 입력
260 # 초콜릿의 무게가 바뀌었다.
360
290
```

## int(input()) 의 의미
`int(input())` 을 실행할 때 무슨 일이 벌어진 것일까?

**입력을 받았다.** <br>
input() 은 사용자로부터 입력을 받아, input() 이 있던 자리가,
사용자가 입력한 값으로 치환되는 것과 같은 효과이다.
즉, input() 을 실행하고 여러분이 100 을 입력했으므로
{% highlight python %}
sugar = int("100")
{% endhighlight %}
을 한 것과 마찬가지다.

**입력한 값의 자료형은 '문자열' 이다.** <br>
input() 은 받은 모든 입력을 '문자열' 자료형으로 만든다.
여러분이 100 이라는 숫자를 입력했어도, 자료형이 문자열 이기 때문에
이를 숫자 자료형, 그 중에서도 정수로 바꾸어야 한다.

**int() 는 문자를 정수로 바꾼다.** <br>
int("100") 은 `문자열 100을 정수로 바꿔라!` 라는 뜻이다.
즉 그 결과는 `정수 100` 이 되고 결과적으로 정수 100 이 sugar 변수에 할당된다.

input() 이 모든 값을 문자열로 해석하는 건, 파이썬을 처음 만들 때 그렇게 '약속' 을 
해서 그렇다. 이는 이해의 대상이 아니라, '암기'의 대상이다.
{: .text-center}
{: .notice--info}

인터프리터를 열어서 type(input()) 을 실행해 보고 아무 값이나 마구 넣어보자.
그 결과는 항상 'str' 일 것이다.
{: .text-center}
{: .notice--info}


