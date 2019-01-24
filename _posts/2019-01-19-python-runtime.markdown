---
layout: single
title:  "파이썬 런타임은 도대체 어떻게 동작하는 것이죠?"
date:   2019-01-19 18:21:03 +0900
categories: [python]
---

<h2>질문</h2>
Stack Exchange 에서 흥미로운 글을 발견해서 이를 번역해 보았습니다.

python 런타임은 실제로 어떻게 동작하나요? 저는 runtime library의 컨셉을 이해하는데 어려움을 겪고 있습니다. 
특히 python의 경우에요. 그래서 python 으로 hello world 프로그램을 작성해서 실행해 보았습니다.
<br><br>
제가 '엔터 버튼을 누르는 것'과  '기계어로 번역된 파이썬 코드가 CPU 에서 실행되는 것' 사이에 어떤 단계를 거치게 되나요? 
그리고 이 과정이 Python runtime 과는 어떤 관계가 있나요?


<h2>답변</h2>
프로그래밍 언어들이 다양한 만큼, 현대 프로그래밍 언어들이 서로 공유하고 있는 공통 컨셉(개념)들이 꽤 있습니다. 
그 중 2 가지가 질문의 답에 핵심이 될 수 있습니다.

"제가 '엔터 버튼을 누르는 것'과 '기계어로 번역된 파이썬 코드가 CPU 에서 실행되는 것' 사이에 어떤 단계를 거치게 되나요?"
{: .text-center} 

작성된 코드는 parse, analyze 를 거쳐서 인터프리터에게 들어갑니다. 본 내용은 전부 compiler 이론과 깊은 관련이 있는데, 
여기서 '컴파일러'는 '코드를 한 언어에서 다른 언어로 번역하는 프로그램'을 말합니다.(보통은 기계어로 번역하는 일을 합니다.) 
몇 년에 걸쳐 연구 할 만큼 방대한 분야이지만, 여기서는 기본적인 얘기만 하도록 하겠습니다.
<br><br>
parser: compiler 는 parser 부터 시작합니다. 소스 코드를 읽어들인 후 문법에 맞춰서 과연 이 소스 코드가 말이 되는지 판단합니다. 
질문자의 경우에는 질문자가 작성한 헬로우 월드 코드가 Python 의 문법에 맞는지 검사하겠죠. 만약 문법이 틀렸다면 parser 가 에러를 낼 것이고 
컴파일링은 중단됩니다. 그러나 만약 문법에 부합한다면 parser는 그 결과로 추상 문법 트리(AST, Abstract Syntax Tree)를 만들어 냅니다. 
예를 들어 x = 5 라는 코드가 있었다면

![image-center]({{ site.baseurl }}/assets/images/2019-01-19-python-runtime-01.png){: .align-center}
이런 모양의 트리가 만들어 집니다.{: .text-center} 

semantic analysis: parser 가 AST 를 만들어 낸 이후엔 다음 단계로 접어듭니다. 이 AST가 무슨 의미인지 알아내는 과정입니다. 
parse 는 통과 했어도 이 단계에서 에러가 일어날 수도 있습니다. (예를 들어 1개의 인자를 받는 함수를 호출 할 때 
3개의 인자를 전달했을 경우) 만약 에러가 없다면 AST를 좀 더 기계가 이해하기 쉽도록 교정합니다.
<br><br>
code generation: 앞서 두 단계를 거치면서 완벽히 분석되고, 간략화 된 AST 를 얻어냈습니다. 이제 이 AST를 generator에 
넣습니다. generator 가 AST를 다른 언어로 번역해서 내보냅니다.(질문자의 경우에는 Python Code 를 기계어로 번역합니다.) 
이로써 compile이 완료됩니다.
<br><br>
파이썬의 경우에는 compiler 가 아니라 interpreter 를 사용합니다. interpreter 는 compiler 와 정확히 똑같이 동작합니다. 
다만 한 가지 차이가 있는데, code 를 번역해서 그 결과를 밖으로 내보내는 것 (파일에 작성하는 등)이 아닌, memory에 로드 
시켜서 바로 실행한다는 것입니다.


"그리고 이 과정이 Python runtime 과는 어떤 관계가 있나요?"
{: .text-center} 

모든 프로그래밍 언어(매우 간단한 언어를 제외하고)는 사전에 정의된 함수를 갖고 있습니다. 
이 함수들은 매우 많은 유저들에게 중요하면서도, 유저들이 직접 정의해서 쓰기는 어려운 함수들입니다.
(print 를 예로 들 수 있습니다. print 함수는 stdout 을 통해 값을 내보내는데, 만약 직접 구현해 보실려고 한다면, 
행운을 빕니다 ^^) 유저들은 여타 라이브러리의 도움을 받지 않고도 실행 중(run time)에 이런 함수들을 쓸 수 있습니다. 
이 함수들이 모여 있는 라이브러리를 runtime 이라고 부르는 것도 그 때문입니다.


<h2>참조</h2>
<a target="_blank" href="https://softwareengineering.stackexchange.com/questions/313254/how-does-the-python-runtime-actually-work">
https://softwareengineering.stackexchange.com/questions/313254/how-does-the-python-runtime-actually-work
</a>

