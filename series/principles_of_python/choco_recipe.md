---
title:  "간단한 계산하기"
date:   2019-07-10 20:21:03 +0900
---

## 초코 레시피
세상의 모든 음식이 그렇듯이 초코도 레시피가 중요하다.
카카오와 각 재료들을 어떤 비율로 섞을 것인지가 초코의 맛을 좌우한다.
우유를 많이 넣으면 밀크 초코, 카카오의 비율이 높으면 다크 초코가 되기도 한다.

![image-center]({{ site.baseurl }}/assets/images/2019-07-10-mixing-choco.jpg){: .align-center}

초코를 만들기 위해 먼저 초코 레시피가 필요한데,
파이썬으로 정확한 초코 레시피를 만들기 위해서 우선 숫자를 표현하는 방법을 알아보자.
숫자를 표현하고, 이를 저장해두었다가 다시 꺼내 쓰고, 더하고 빼고 나누고 곱하는 방법 등을 알아보자.


## 콘솔 열기
우선 파이썬 콘솔을 열어보자.
`Pycharm` 을 사용하고 있다면 화면 하단의 `Python Console` 을 클릭하면 열린다.<br>
윈도우 사용자라면 윈도우키를 누른 후 python 을 입력 후에 Enter 를 쳐서 열 수도 있다.
![image-center]({{ site.baseurl }}/assets/images/2019-07-10-console.jpg){: .align-center}

위 이미지와 같이 마지막 줄에 `>>>` 표시가 나타난다면 콘솔을 여는데에 성공한 것이다.


## 기본적인 + - * /
먼저 *일반 초코*를 만드는데
카카오 60g 설탕 120g, 우유 100g 이 필요하다고 가정하자. (실제로 이 레시피대로 초코를 만들어 먹지는 말자.
맛을 보장하지 않는다.) 만들어질 초코의 무게는 얼마나 될까? 

```일반 초코의 레시피 = 카카오 60g + 설탕 120g + 우유 100g```

파이썬 콘솔에 다음을 입력해보자. (카카오 60, 설탕 120, 우유 100 의 순서이다.)
{% highlight python %}
>>> 60 + 120 + 100
280
{% endhighlight %}
완성품 초코의 무게는 280g 이 될 것이다.

<br>
*밀크 초코*를 만드는 데에는 우유가 100g 더 들어간다고 해보자.
{% highlight python %}
>>> 60 + 120 + 200
380
{% endhighlight %}

<br>
*다크 초코*를 만드는 데에는 카카오가 30g 더 들어간다고 하면
{% highlight python %}
>>> 90 + 120 + 100
310
{% endhighlight %}

이렇게 간단하게 3가지 초코의 레시피와, 그 결과물 초코의 무게를 계산해 보았다.


## 설탕량 할당
기본적으로 3가지 초코를 만들 때에 들어가는 설탕의 양은 120g 으로 똑같았다.
그렇다면 일일이 120 이라는 숫자를 입력할 것이 아니라, '설탕' 이라고
입력하면 바로 120이 들어가도록 만들면 편하지 않을까?
파이썬 콘솔에 다음과 같이 입력해보자.

{% highlight python %}
>>> sugar = 120
>>> 60 + sugar + 100
280
{% endhighlight %}

놀랍게도 120 대신에 sugar 를 넣었는데 계산이 되었다! 무슨 일이 일어났는지 설명하겠다. 

우리가 방금 입력한 `sugar = 120` 을 `할당` 이라고 부른다. 120 이라는 숫자를 할당한 것이다.
어디에 할당했냐면, `sugar` 에 할당했다.

여기서 `sugar` 는 `변수` 라고 한다. 변수는 값을 저장하는 공간을 말한다.
즉,
{% highlight python %}
>>> sugar = 120
{% endhighlight %}
는 파이썬에서 다음과 같은 의미이다.

**sugar 라는 이름의 변수에 120 을 저장하겠다!**
{: .text-center}
{: .notice--info}

## 변수 할당
그럼 아까 sugar = 120 을 했던 것 처럼 이제는 초코, 밀크 초코, 다크 초코에 각각 이름을 붙여주자.
{% highlight python %}
>>> sugar = 120
>>> choco = 60 + sugar + 100
>>> milk_choco = 60 + sugar + 200
>>> dark_choco = 90 + sugar + 100
{% endhighlight %}

이름을 다 지어주었는가? 그렇다면 이제부터 콘솔에 아무 초코의 이름을 입력하고 Enter 를 눌러보자.
{% highlight python %}
>>> milk_choco # 380 출력
{% endhighlight %}
milk_choco 의 무게가 잘 `할당` 되었음을 확인할 수 있다!

## 변수의 값 변경
변수는 그 단어 뜻 그대로 "변할 수 있는 수" 이다. 필요하다면 언제든지 변수의 값을 바꿀 수 있다.
예를 들어보겠다.

레시피대로 다크 초코를 만들어 먹어보니, 생각보다 덜 다크했다고 하자.
더 다크하게 만들기 위해서 카카오의 함량을 90이 아니라 120 으로 해 보겠다.
{% highlight python %}
>>> dark_choco
310
>>> dark_choco = 120 + sugar + 100
>>> dark_choco
340
{% endhighlight %}
변수 dark_choco 의 값이 바뀌었다. 이것으로 좀 더 다크한 다크초코가 만들어 졌을 것이다.

## 곱하기
밀크 초코를 다음과 같이 정의할 수도 있다.
{% highlight python %}
>>> sugar = 120
>>> milk = 100
>>> milk_choco = 60 + sugar + milk * 2
{% endhighlight %}
milk 에 2를 곱해 200 으로 만든 것이다. 보통 컴퓨터에서 곱하기를 표현할 때에는 * 를 사용하는데,
영어 x 와 구별하기 위해서이다.


## 나누기
그렇다면 나누기는 어떻게 할까? 이번에는 아래의 해답을 보지 말고 여러분 스스로 해 보자.
카카오가 일반 초코의 절반 만큼 들어간 초코를 mild_choco 라고 할 때,
이 mild_choco 레시피를 만들어 보자. 아마 여러분의 예상과 조금 다른 답이 나올것 같다.

<script>
function showAnswerChocoDiv() {
    document.getElementById("answer").style.display='block';
    document.getElementById("answer2").style.display='block';
}
</script>
<button class="btn btn--info align-center" onclick="showAnswerChocoDiv()">정답보기</button> 

<div id="answer" style="display:none;">
{% highlight python %}
>>> sugar = 120
>>> milk = 100
>>> mild_choco = 60 // 2 + sugar + milk
{% endhighlight %}
</div>

<p id="answer2" style="display:none;">
아마 여러분은 <code class="highlighter-rouge">/</code>을 사용해서 계산을 했을 것이다.
/ 을 사용해서 계산했을 경우, mild_choco 의 값이 
250이 아니라 250.0 으로 보일 것이다. 왜 그런지는 다음 장을 넘겨서 확인해 보자.
</p>

빼기는 여러분의 예상 대로 `-` 기호를 사용하면 된다. 설명은 생략한다.
{: .text-center}
{: .notice--info}


## 정리하기
* 수학 시간에 배운 + - / * 를 파이썬에서도 그대로 사용할 수 있다.
* 변수는 값을 저장하는 공간이다.
* 변수의 값은 변할 수 있다.





