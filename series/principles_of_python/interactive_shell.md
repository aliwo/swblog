---
title:  "인터렉티브 쉘"
date:   2019-01-19 20:21:03 +0900
---

## 파이썬을 실행시키는 2가지 방법

파이썬 인터프리터를 실행시키는 데에는 2가지 방법이 있다.
* 파이썬 스크립트 파일을 작성하고, 해당 파일을 인터프리터에게 전달한다.
* 인터프리터 모드로 실행한다.

오늘은 인터프리터 모드로 실행하는 방법을 알아보자.

## 인터프리터 모드 실행
윈도우의 경우 python3 를 환경변수 PATH 에 등록해야만 아래 내용을 따라갈 수 있다.
만약 python 을 입력했는데 

```markdown
'python'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
배치 파일이 아닙니다. 
```

이런 메세지가 나타난다면 환경변수 PATH 를 확인해 보시길 바란다.

터미널에서 python (리눅스나 mac 의 경우에는 python3) 를 입력하면 파이썬을 인터프리터 모드로
실행할 수 있다.

```html
C:\Users\경로>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```


## 파이참에서 인터프리터 모드 실행하기
파이참 하단의 tool window bar 에서 'Python Console' 을 클릭하면 자동으로
인터프리터 모드로 python 이 실행된다.

![image-center]({{ site.baseurl }}/assets/images/2019-01-24-pycharm-console.jpg)

## 인터프리터 실행과 스크립트 실행의 차이점

크게 2가지 차이점이 있다.
인터프리터 모드일 때

* \>\>\> 이 나타난다.
* 변수의 이름을 입력하고 Enter 를 누르는 것 만으로 변수의 값을 출력(화면에 나타난다)한다.
{% highlight python %}
>>> my_number = 7
>>> my_number
7 # 변수 안의 값 출력
{% endhighlight %}


보통 인터프리터 모드는 간단하게 테스트 해보고 싶은 게 있을 때 적합하고
제대로 파이썬 프로그램을 만들때는 파일을 만들어 그 안에 작성하는게 보통이다.








