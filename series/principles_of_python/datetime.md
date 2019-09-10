---
title:  "DateTime"
date:   2019-09-09 11:21:03 +0900
---

![image-center]({{ site.baseurl }}/assets/images/2019-09-09-choco2.jpg){: .align-center}

## 날짜와 시간을 다루는 방법
초콜릿 하면 떠오르는 것 중에서 '제조일자'와 '유통기한' 도 있었다.
그렇다면 파이썬 프로그램에서 날짜와 시간을 표현하려면 어떻게 해야 할까?

## datetime 모듈
파이썬에서 날짜와 시간을 저장하고 조작하기 위해서는
`datetime` 모듈을 사용한다. 
여기서 `모듈`은 '정해진 임무를 수행하기 위해 만들어진 
파이썬 함수, 클래스등이 한 파일에 모여있는 것'이라고 생각하면 된다.

이름에서 알 수 있듯이 datetime 모듈은 
날짜와 시간과 관련된 기능을 제공하기 위해 만들어 졌다.
파이썬 콘솔을 열어서 따라해보자.

{% highlight python %}
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2019, 9, 9, 15, 22, 19, 941214)
{% endhighlight %}

`from ... import ...` 혹은 `import ...` 을 사용해서 모듈을 가져올 수 있다.

`from datetime import datetime` 은 datetime 모듈로 부터 datetime 클래스를
가져오라는 뜻이다. 

`datetime.now()` 메소드를 실행하면 현재 시각을 담고 있는
datetime 객체가 반환된다. 여러번 실행해 보자.

{% highlight python %}
type(datetime.now())
<class 'datetime.datetime'>
{% endhighlight %}

## datetime 활용하기

초코가 만들어지는 순간 제조일자를 기억하도록 하고 싶다면
다음과 같이 하면 된다.

{% highlight python %}

class Choco:

    def __init__(self, sweetness):
        self.created_at = datetime.now()
        self.sweetness = sweetness

{% endhighlight %}


## datetime 포매팅

이번엔 초코의 설명을 정갈한 텍스트에 담아서 리턴하는 메소드를 만들어 보자.
초코의 '자기소개문' 이다.

{% highlight python %}

class Choco:

    def __init__(self, sweetness):
        self.created_at = datetime.now()
        self.sweetness = sweetness

    def format_report(self):
        created_at = self.created_at.strftime('%Y-%m-%d')
        return f'{created_at} 에 생산된 초콜릿입니다. ' \
               f'\n맛은 {self.sweetness}입니다.'

{% endhighlight %}

다 만들었다면 실행해 보자.

{% highlight python %}
print(Choco(5).format_report())
print(Choco(2).format_report())
{% endhighlight %}

잘 실행되는 것을 확인할 수 있다.

## f 스트링
앞의 예제를 따라해보면서 `f'문자열''` 에 대해 궁금해졌을 것이라고 생각한다.
사실 파이썬에서 문자열 포매팅(문자열 안에 값을 적절히 집어넣는 것)을 하는 방법이
여러가지가 있다.





