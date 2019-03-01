---
title:  "딕셔너리"
date:   2019-01-19 20:21:03 +0900
---


## 도라에몽

![image-center]({{ site.baseurl }}/assets/images/doraemong.jpg){: .align-center}

진구 曰:“도라에몽, 날도 추운데 모히또 가서 몰디브나 한 잔 할까?”
{: .text-center}

도라에몽 曰: "좋아~"
{: .text-center}

도라에몽은 자신의 도구 주머니에서 ‘어디로든지 문’을 찾기 시작한다.
도라에몽의 도구 주머니는 리스트 타입으로 되어 있다.

{% highlight python %}

gadget_list = [
    '공기총',
    '대나무 헬리콥터',
    '울트라링',
    '우정 캡슐',
    '월광등',
    '이어주는 실',
    '패션 카메라',
    '화해하는 종',
    '호랑이 꼬리 세트',
    '로빈슨 크루소 세트',
    '어디로든지 문'
    '로켓 빨대',
    '빅 라이트',
]

{% endhighlight %}


도라에몽은 0번째 인덱스부터 ‘어디로든지 문’ 을 찾아나간다.
{% highlight python %}
gadget_list[0] # 공기총
{% endhighlight %}

0번째 인덱스에는 공기총이 들어있었다. 도라에몽은 탐색을 계속한다.
{% highlight python %}
gadget_list[1] # 대나무 헬리콥터
{% endhighlight %}
1번째 인덱스의 도구도 어디로든지 문은 아니었다.


이런 식으로 찾아 나가면 도구를 찾기 까지 한 참이 걸릴 것이다. 필요한 도구가 생각날 때 마다 도구 주머니를 
일일이 찾아나가야만 하는 걸까? 좋은 방법을 생각해보자.

"list.index(‘어디로든지 문’) 함수를 사용하면 되는거 아닌가요?"
{: .text-center}

물론 list.index()를 사용하면 함수 호출 한 번으로 원하는 요소가 몇 번째 인덱스에 있는지 찾을 수 있다. 
그러나 list.index() 함수 안에서 내부적으로 일일이 리스트 안의 요소를 찾아 나간다는 것은 변함이 없다. 
일일이 탐색하지 않고 요소를 찾을 수 있는 방법이 있는데, 바로 딕셔너리에 저장하는 것이다.

## 딕셔너리 소개
딕셔너리는 다음과 같은 특징을 갖고 있다.
* {} (중괄호) 를 사용해서 선언한다.
* 한 요소당 key 값, value 값 두 가지 값을 쌍으로 갖고 있다.
* 리스트에 비해 탐색 연산이 빠르다.
* 숫자 인덱스 대신 key 값을 사용해 value 에 접근한다.
* 파이썬의 딕셔너리는 순서가 ‘있는’ 자료형이다.(cpython 버전 3.6 이후 부터, 버전 3.7 이후 부터는 모든 파이선 dict 는 
‘삽입한 순서’를 유지한다. <a target="_blank" href="https://mail.python.org/pipermail/python-dev/2017-December/151283.html">
 https://mail.python.org/pipermail/python-dev/2017-December/151283.html</a> )

간단하게 딕셔너리를 정의해 보자.
{% highlight python %}
gadget_dict = {
    'key 값' : 'value 값'
}
{% endhighlight %}

value 값을 가져오고 싶을 떈  아래와 같이 한다.
{% highlight python %}
print(gadget_dict['key 값']) # 출력 : value 값
{% endhighlight %}

자 이제 아직도 리스트로 된 도구 주머니를 뒤지고 있는 도라에몽에게 돌아가 보자.
도라에몽의 도구를 dict 로 구현하면 아래와 같이 표현할 수 있다.

{% highlight python %}
gadget_dict = {
    '공기총' : '공기총',
    '대나무 헬리콥터' : '대나무 헬리콥터',
    '울트라링' : '울트라링',
    '우정 캡슐' : '우정 캡슐',
    '월광등' : '월광등',
    '이어주는 실' : '이어주는 실',
    '패션 카메라' : '패션 카메라',
    '화해하는 종' : '화해하는 종',
    '호랑이 꼬리 세트' : '호랑이 꼬리 세트',
    '로빈슨 크루소 세트' : '로빈슨 크루소 세트',
    '어디로든지 문' : '어디로든지 문',
    '로켓 빨대' : '로켓 빨대',
    '빅 라이트' : '빅 라이트'
}
{% endhighlight %}


이제 바로 도구를 찾을 수 있겠다.
{% highlight python %}
print(gadget_dict['어디로든지 문']) # 바로 찾았다.
{% endhighlight %}


## 딕셔너리의 기능

또 다른 날, 진구가 도라에몽의 도구 주머니에 대해 질문하기 시작한다.
“주머니에는 도구가 몇 개나 들어 있어?”
“주머니에 들어있는 도구는 무엇 무엇이 있어?”
“새로운 도구를 주머니에 넣으려면 어떻게 해?”
“지금 주머니에 대나무 헬리콥터 있어?”
진구의 궁금증을 풀어줄 수 있는 dict 여러가지 기능을 소개한다.

dictionary 안의 요소 수를 알고 싶으면 len() 을 사용하면 된다.

{% highlight python %}
print(len(gadget_dict))
{% endhighlight %}

dictionary 안의 모든 요소를 조회하고 싶다면 다음 방법들이 있다.

{% highlight python %}
dict.keys() # 모든 key 값들을 반환합니다. 
dict.values() # 모든 value 값들을 반환합니다.
dict.items() # 모든 key, value 쌍을 반환합니다.
gadget_dict['새로운 도구'] = '새로운 도구'
print(gadget_dict.values()) # dict_values(['공기총', '대나무 헬리콥터', '울트라링', '우정 캡슐', '월광등', '이어주는 실', '패션 카메라', '화해하는 종', '호랑이 꼬리 세트', '로빈슨 크루소 세트', '어디로든지 문', '로켓 빨대', '빅 라이트', '새로운 도구'])
{% endhighlight %}


dictionary 안에 특정 key 값이 있는지 조회하려면
{% highlight python %}
print('대나무 헬리콥터' in gadget_dict) # True
gadget_dict.pop('대나무 헬리콥터')
print('대나무 헬리콥터' in gadget_dict) # False
{% endhighlight %}

