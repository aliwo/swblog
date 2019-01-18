---
layout: single
title:  "navigation 문제"
date:   2019-01-16 21:21:03 +0900
categories: [jekyll]
---

<h2> navigation 에서 현재 항목이 강조표시되지 않는 문제 </h2>
minimal mistake의 docs page 에 들어가보면 왼쪽에 네비게이션 사이드바가 보입니다.
네비게이션을 통해 아무 항목에나 들어가 보겠습니다. 들어가서 다시 네비게이션 사이드바를 보면
지금 보고 있는 페이지의 제목이 강조(bold) 표시 된 것을 알 수 있습니다.
<br><br>
그런데 처음 

<h2>First Try</h2>
커스텀 자바스크립트를 포함해, sidebar navigation의 항목을 jquery로 찾아낸 뒤
현재 url과 똑같으면 

처음에는 크롬 디버거를 사용해서 html 태그에 class 가 붙는 타이밍을 체크하려고 했습니다.
마우스 클릭, 커서 올려 놓음, 키 입력 등에 리스너를 달 수는 있지만 특정 엘레멘트의
클래스가 변했는지 여부는 파악하는 방법을 몰랐습니다.

또한 jekyll 에 의해 생성된 html 에서 active 클래스가 

<h2>Second Try</h2>



<h2>해결</h2>