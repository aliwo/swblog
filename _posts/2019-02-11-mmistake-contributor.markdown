---
layout: single
title:  "Minimal Mistake 버그 픽스"
date:   2019-02-01 09:21:03 +0900
--- 


## 발단

![image-center]({{ site.baseurl }}/assets/images/2019-02-11-toc.jpg){: .align-center}

사진은 minimal mistake 퀵 스타트 가이드의 toc
{: .text-center} 

테마 Minimal Mistake 에는 페이지, 포스팅의 내용을 읽어서
자동으로 table of contents(줄여서 toc) 를 생성해 주는 편리한 기능이 있다.

본문 내용에 
* h2 부제1
* h2 부제2
* h3 부제3 

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

뭐가 문제인 것일까...

![image-center]({{ site.baseurl }}/assets/images/2019-02-11-err-body.jpg){: .align-center}

그런데 가만히 보니 이 %와 16진수의 향연... 어딘가 익숙하다.
{: .text-center} 

http 공부를 할때 많이 보던 URL escape 문자열이다. 확인차 URL Encoder, Decoder 를 돌려보니
내가 클릭했던 헤더의 제목이 나왔다.

아무래도 URL escape 된 한글 값이 그대로 자바스크립트 함수 어딘가에 들어가고 있는 모양이다.


## Minimal Mistake Contributor 가 되었습니다.
히히



## 링크
<a href="https://github.com/mmistakes/minimal-mistakes/pull/2042" target="_blank"> 여기 </a> 

