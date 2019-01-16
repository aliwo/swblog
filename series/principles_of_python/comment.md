---
title:  "주석"
date:   2019-01-14 20:21:03 +0900
---



인간은 읽을 수 있고, 로봇은(혹은 악성 프로그램을) 읽을 수 없는 이미지를 CAPTCHA(Completely Automated Public Turing test to tell Computers and Humans Apart) 라고 한다. 보통 회원가입을 할때나 콘서트 예매를 할 때 볼 수 있다.
이처럼 프로그래밍에서도 사람만 읽고, 프로그램은 무시하도록 만들어진 코드를 '주석' 이라고 한다. 주석은 보통 다른 개발자('미래의 나'를 포함해서)를 위해 코드에는 드러나지 않은 배경지식을 설명하거나, 복잡한 코드를 쉽게 설명하기 위한 용도로 작성한다.



주석 적기

파이썬의 한 줄 주석(inline comment)은 # 으로 표현한다. # 으로 시작하는 부분은 인터프리터가 무시하고 지나간다.
{% highlight python %}
# 한 줄 주석 입니다.
{% endhighlight %}


내용이 길어서 주석을 여러 줄(multi-line comment)에 걸쳐 나눠서 쓰고 싶다면 # 을 연달아서 사용한다.

# 여러줄
# 주석, # 이후 한 칸 띈 다음 적습니다.
# 이렇게 적습니다.



여러 줄 주석을 작성할 때 """ 혹은 ''' 을 사용할 수도 있는데, 이는 엄밀히 말해서 주석이 아니다. 파이썬 스타일 가이드 (PEP8, https://www.python.org/dev/peps/pep-0008/#block-comments)은 연속으로 # 을 써서 여러 줄 주석을 표현할 것을 권장하고 있으니, ''' 은 삼가하도록 하자.

"""여러 줄 
엄밀히 말해 주석은 아닙니다."""

'''되도록이면 #을
 연달아 사용하도록 합시다'''



 ''' 혹은 """ 으로 둘러쌓인 부분은 무시되지 않는다.

hi = '''엄밀히 말해
 주석은 아니다.'''

print(hi) # 출력 값 : 엄밀히 말해\n 주석은 아니다. 



코드 블록


기본적으로, 한 line 당 한 문장을 작성하고, 개행한다.

my_variable = 3
print(my_variable) 


한 Line 에 여러 문장을 작성하고 싶다면 방법은 있습니다. ;(세미콜론)을 사용하면 됩니다. 그러나 권장되는 방법은 아닙니다.

my_variable = 3; print(my_variable) # 출력: 3 


파이썬은 함수 블록 혹은 클래스 블록을 표현하기 위해 {}'중괄호' 를 사용하지 않습니다. 대신 tab (혹은 space bar 4번)을 사용해서 들여씁니다.

class MyClass:
    my_variable = 3
    my_second_variable = 4



참고: https://www.python.org/dev/peps/pep-0008/




읽을거리


주석이 없어서 벌어진 일: http://m.thisisgame.com/webzine/nboard/257/?n=61912



