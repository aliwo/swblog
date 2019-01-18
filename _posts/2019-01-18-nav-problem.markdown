---
layout: single
title:  "side bar navigation 문제"
date:   2019-01-16 21:21:03 +0900
categories: [jekyll]
---

<h2> navigation 에서 현재 항목이 강조표시되지 않는 문제 </h2>

![image-center](/assets/images/2019-01-18-nav-1.jpg){: .align-center}

빨간 밑줄, Bold로 강조 표시 되어 있습니다.
{: .text-center}

minimal mistake의 docs page 에 들어가보면 왼쪽에 네비게이션 사이드바(이하 네비게이션)가 보입니다.
이 기본 네비게이션은 현재 보고 있는 항목의 제목을 강조(bold) 표시해 주는 기능이 있습니다. 
위 스크린샷을 보시면 현재 Structure 항목을 보고 있기 때문에 해당 항목이 Bold 로 강조된 것을 확인할 수 있습니다. 
<br><br>
```yaml
# _data/navigation.yml
# 초략
pop:
  - title: 안녕? 난 파이썬이라고 해
    children:
      - title: "들어가며"
        url: /series/principles_of_python/intro/index.html
      - title: "파이썬 설치"
        url: /series/principles_of_python/install_python/index.html
      - title: "개발환경 설치"
        # 후략
```
제 블로그에도 같은 네비게이션을 간단한 설정 만으로 적용할 수 있었습니다. 
적용한 네비게이션은 url 링크도 잘 작동했고, 디자인도 예쁘고 깔끔해 만족하고 있었습니다.
다만 적용 하루 이후에 네비게이션을 다시 보니
공식 문서 페이지에서는 있었던 '강조 표시 기능'이 제 블로그에서는 작동하지 않고 있음을 발견했습니다. 
<br><br>

![image-center](/assets/images/2019-01-18-nav-2.jpg){: .align-center}

'들어가며' 항목을 보고 있는데도 네비게이션의 '들어가며'는 Bold 처리되지 않음.
{: .text-center}

뭐가 문제인지 알아내기 위해 구글링을 시작했습니다.


<h2>First Try</h2>
네비게이션을 커스텀 할 수 있는, 제가 아직 모르는 설정이 어딘가에 있는건지 먼저 찾아 보았습니다.
minimal mistake 안에 이미 적용된 기능을 사용하는 편이 제가 직접 커스텀 하는 것 보다
버그가 발생활 확률도 적고(minimal mistake는 이미 테스트를 거쳐서 배포됬기 때문에) 수고도 덜 드니까요.

하지만 공식 문서에서는 sidebar 를 만들고 나서 바로 끝나버립니다. 바로 다음 내용으로 넘어갔습니다.
구글링에서 들어간 Github issue 에서도 url이 404 에러를 내는 문제의 해결 글 
등등은 찾았지만, 제가 찾는 답은 없었습니다. 
깃허브에서 원본 소스의 data/navigation.yml 을 조사해 봤지만 거의 비어 있어서
역시 건질만한 것은 없었습니다.

크롬 디버거를 사용해서 조사했을때 '강조표시' 되어 있는 a 태그에만 class="active" 가
붙어 있는 것을 확인했습니다. 웹 프론트 개발 하면서 많이 본 패턴입니다.
보통 이런 패턴이라면 대상(네비게이션)이 전부 렌더링 된 이후,
혹은 document 가 ready 이벤트를 발생시켰을때,
제이쿼리를 사용해 네비게이션 목록을 조사해 현재 url (혹은 항목의 제목)과
서로 일치하는 값을 가진 네비게이션 항목에 'active' 클래스를 붙여주는 것이라고 추측했습니다.

이제 해당 자바스크립트 코드가 어디있는지를 찾아내 문제를 잡아내면 됩니다. 그러나
페이지 소스 전체에서 'active'를 검색해도 나오는 것은 uglified 된 자바스크립트라 
대체 코드가 뭘 하고 있는건지 파악하기는 어려웠습니다.

다시 막혔습니다.

<h2>Second Try</h2>

minimal mistake의 기본 설정만으로 해결할 수 없다면 커스텀 자바스크립트를 추가하는 방법을 찾아보기로 했습니다.
그런데 이것도 쉬운 일은 아닙니다. 일반적인 html 파일이었다면 네비게이션.html 을 찾아서 
해당 파일 제일 밑에 \<script type="text/javascript"\> 
로 자바스크립트 코드만 추가하면 되는 일입니다만 jekyll 에 의해서 html 파일이 생성되는 구조였기 때문에
그렇게 할 수는 없었습니다. 생성된 파일을 수정해봤자 다음 번 생성때 증발하고 마니까요. 

다시 검색을 반복. jekyll 공식 문서에서 _include 의 존재를 알게 되고 다음과 같은 아이디어를 얻습니다.
1. navigation 을 찾고, 현재 url 을 가져와서 비교 후 항목을 강조하는 자바스크립트 코드를 작성.
2. _include 안에 html 파일을 하나 만들어 해당 코드를 삽입
3. 파이썬 씨리즈의 모든 md 파일에서 해당 html 파일을 include.

그러나 새로운 글을 적을 때 마다 파일을 include 해야 한다는 점이 너무 번거롭다고 생각했습니다.

<h2>Third Try: 해결</h2>
한 번 더 minimal mistake github 를 뒤져 봤습니다. 앞서 _include 디렉터리의 존재를
알게 되어서인지 그쪽으로 눈이 갔습니다. 거기서 찾은 것은 파일 'nav_list'. 

```markdown
{%- raw -%} 
{% comment %} set "active" class on current page {% endcomment %}
{% if child.url == page.url %}
  {% assign active = "active" %} 
{% endraw %} 
```
위 라인을 읽고 나서 새로운 설정을 찾을 필요도, 자바스크립트를 작성할 필요도 없다는 걸 바로 깨달았습니다.

page.url과 yml의 url이 다른게 문제였구나.
{: .text-center}

그래서 아무 페이지에서 page.url 을 출력해 보았는데, /series/principles_of_python/<항목>/ 형식이라는 것을 알게 됩니다.
제가 yml 에 적었던 url 은 /series/principles_of_python/<항목>/index.html 이니, 서로 일치하지 않습니다.
각 url 마다 index.html 부분만 삭제해주면 일치하게 됩니다.

```yaml
# _data/navigation.yml
# 초략
pop:
  - title: 안녕? 난 파이썬이라고 해
    children:
      - title: "들어가며"
        url: /series/principles_of_python/intro/index.html # page.url 과 맞지 않음.
      - title: "파이썬 설치"
        url: /series/principles_of_python/install_python/ # page.url 과 일치함. 모든 url 을 이와같이 바꿔야 함.
      - title: "개발환경 설치"
        # 후략
```


<h2>결과</h2>

![image-center](/assets/images/2019-01-18-nav-3.jpg){: .align-center}

깔끔하게 해결
{: .text-center}
