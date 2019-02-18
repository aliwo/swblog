---
layout: single
title:  "Minimal Mistake 버그 픽스"
date:   2019-02-01 09:21:03 +0900
categories: [minimal-mistake]
--- 


## 발단

![image-center]({{ site.baseurl }}/assets/images/2019-02-11-toc.jpg){: .align-center}

사진은 minimal mistake 퀵 스타트 가이드의 toc
{: .text-center} 

테마 Minimal Mistake 에는 페이지, 포스팅의 내용을 읽어서
자동으로 table of contents(줄여서 toc) 를 생성해 주는 편리한 기능이 있다.

본문 내용에 
* h2 부제목1
* h2 부제목2
* h3 부제목3 

이 존재한다면 부제1,2,3 을 toc 에 넣어주는 형식이다. 
front matter 에서 toc:true 만 설정해 주면 한 방에 생성되므로
필자도 파이썬 강의록에 잘 쓰고 있었다.

열심히 파이썬 강의록을 작성하던 도중, 자동으로 생성된 table of contents 의
링크 기능이 작동하지 않는 다는 것을 발견.
개발자 도구를 열어보니 Syntax Error 경고가 뜨고 있다는 것을 알게 되었다.

![image-center]({{ site.baseurl }}/assets/images/2019-02-11-syntax-err.jpg){: .align-center}

빨간 원 부분을 클릭해도 해당 헤더로 넘어가지 않고 에러만 뜸.
{: .text-center} 

읭? 새로고침, jekyll serve 다시 시작 등등...  여러가지를 시도해 보았지만
같은 에러메세지만 보인다. 일시적인 에러는 아닌 것 같았다.

## 원인 분석
자동생성된 컨텐츠다 보니 아직 minimal mistake 나 jekyll 의 작동방식에 익숙하지 않아
어디가 문제인지 짐작도 가지 않는 상황.

구글 검색으로도 만족할만한 답변은 찾지 못했다. 

크롬 javascript 디버깅도 시도해 봤는데 이미 minified 된 파일이라 봐도 뭐가 뭔지를 모르겠다.
(minified 된 코드를 해독하려고 시도해봤지만 눈 아파서 포기했다^^)

뭐가 문제인 것일까...

멍하니 에러코드만 바라보고 있었다.

![image-center]({{ site.baseurl }}/assets/images/2019-02-11-err-body.jpg){: .align-center}

그런데 가만히 보니 이 %와 16진수의 향연... 어딘가 익숙하다.
{: .text-center} 

http 공부를 할때 많이 보던 URL escape 문자열이다. 확인차 URL Encoder, Decoder 를 돌려보니
내가 클릭했던 헤더의 제목이 나왔다.

```markdown
%ED%95%A8%EC%88%98%EC%9D%98%20%ED%98%B8%EC%B6%9C -> 함수의 호출
```

아무래도 URL escape 된 한글 값이 그대로 자바스크립트 함수 어딘가에 들어가고 있다는 의심을 하게 되었다.

## 문제 해결

mmistake quick 가이드를 통해 js 파일의 위치는 알게 되었다. 그 위치는 **assets/js/_main.js** 이다.
아마 Gem 으로 블로그를 설치했다면 처음에 이 파일이 없기 때문에, 깃허브에서 복사해서 가져온 것으로 기억한다.
가져온 _main.js 파일을 수정한 후 npm 으로 빌드에 성공하면 자바스크립트 수정은 완료다.

그렇다면 _main.js 에서 escape 된 url 문자열이 들어가는 부분을 찾으면 된다.

비록 minified 되어 있긴 하지만 에러 스택과 _main.js 를 번갈아 보면서
```markdown
main.min.js:6 Uncaught Error: Syntax error, unrecognized expression: #%EB%B0%98%EA%B0%91%EC%8A%B5%EB%8B%88%EB%8B%A4
    at Function.oe.error (main.min.js:6)
    at oe.tokenize (main.min.js:6)
    at oe.select (main.min.js:6)
    at Function.oe [as find] (main.min.js:6)
    at S.fn.init.find (main.min.js:6)
    at new S.fn.init (main.min.js:6)
    at S (main.min.js:6)
    at Function.v.smoothScroll (main.min.js:6)
    at main.min.js:6
    at dispatch (main.min.js:6)
```

함수 smoothScroll 를 검색해 보았다. 아래는 _main.js 의 일부 


```javascript
// 초략
  // Smooth scrolling

  // Bind popstate event listener to support back/forward buttons.
  var smoothScrolling = false;
  $(window).bind("popstate", function (event) {
    $.smoothScroll({
      scrollTarget: location.hash,
      offset: -20,
      beforeScroll: function() { smoothScrolling = true; },
      afterScroll: function() { smoothScrolling = false; }
    });
  });
  // Override clicking on links to smooth scroll
  $('a[href*="#"]').bind("click", function (event) {
    if (this.pathname === location.pathname && this.hash) {
      event.preventDefault();
      history.pushState(null, null, this.hash);
      $(window).trigger("popstate");
    }
  });


// 후략
```
찾았다.

**scrollTarget: location.hash,** 에서 location.hash 가 그대로 들어가는 게 문제라고 확신하게 되었다.
그래서 

```javascript
scrollTarget: decodeURI(location.hash) // scrollTarget: location.hash,
```
이렇게 바꿔주었더니

문제는 깔끔하게 해결. location.hash 를 사용하는 부분이 몇 개 더 있었는데, 
해당 코드도 decodeURI 함수로 감싸 주었다.


## Minimal Mistake Contributor 가 되었습니다.

npm 으로 빌드 했더니 깔끔하게 고쳐진 것이 확인되었다. 뿌듯하다.

좋은 건 나눠가지는 거라 했던가. 이 버그 픽스를 다른 minimal mistake 사용자들도
누려야 한다는 생각이 들었다.

설레이는 마음으로 minimal mistake 깃허브에 pull request 를 날렸다.

![image-center]({{ site.baseurl }}/assets/images/2019-02-14-bugfix.jpg){: .align-center}

깔끔하게 merge 되었다!
{: .text-center} 



## 링크
<a href="https://github.com/mmistakes/minimal-mistakes/pull/2042" target="_blank"> 여기 </a> 

