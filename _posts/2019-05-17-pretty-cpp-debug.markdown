---
layout: single
title:  "원숭이도 따라한다! c++ vector 내용 디버깅하기"
date:   2019-05-17 19:10:03 +0900
categories: [c++, gdb]
--- 

## 들어가며
원숭이도 따라한다! 2번째 시리즈입니다.
이번에는 C++ 에서 디버깅 하며 vector 안의 내용을 볼 수 있게 하는 방법을 알아보겠습니다.

먼저, 제가 사용하는 환경은 Windows10, VsCode(C++ extension, Code Runner), MinGw 라는 것을 알려드립니다.

일반적으로 C++ 을 디버깅할 때 Variables 탭에서 vector 안을 조사해 보면 Vector의 정의만 보입니다.
```
std::_Vector_base<int, std::allocator<int>  > (base): ...
```

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp01.jpg){: .align-center}
선생님... vector 안이 보이지가 않아요
{: .text-center }

그러나 Vector 의 정의가 보고 싶어서 디버깅을 누르는 개발자가 있을까요? 우리가 원하는건
현 시점에 백터 안에 어떤 요소가 들어있는지 입니다.

알아서 딱딱 v[0] 에 뭐가 들어있는지, v[1] 에 뭐가 들어있는지 바로바로 보이면 편할텐데 vs code
에서 그냥 디버깅을 실행하면 그런 것들이 보이지가 않습니다.
 
이런 상황에서는 cout<< 혹은 printf() 로 v[0] 과 v[1] 을 일일이 출력해 보거나,
for 문 반복, iterator 등으로 전부를 출력해 볼 수는 있습니다. 좀 더 나아간다면 gdb 의 -exec print 등을
사용해 볼 수도 있겠죠.

하지만 불편합니다. 매 번 printf() 를 찍는 건 귀찮습니다. 디버깅이 끝나고 printf()를 지우는 건
더 귀찮구요 그냥 F5로 디버깅 할 때마다 바로바로 객체 내부를 한 번에 들여다 보는 방법은 없을까요?

네. 있으니까 이 글이 나왔겠죠. 지금부터 알아보겠습니다. 

**주의:** 이 방법은 MinGw 의 gdb 를 사용하므로, gdb가 아닌 Cygwin 을 사용하시는 분들은
사용할 수 없어요 ㅠㅠ 
{: .notice--info}

## 결과

완료하면 다음과 같이 vector 안의 각 요소가 훤히 보이게 됩니다!
![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp02.jpg){: .align-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp03.jpg){: .align-center}
보인..다아
{: .text-center }

## 순서
전체적인 작업 순서는 다음과 같습니다.
1. Python 기능을 지원하는 MinGw 를 설치합니다. (네, 그 Python 맞습니다. Python2.7 입니다.)
2. 새로운 MinGw 를 사용하도록 tasks.json 을 수정합니다.
3. 새로운 MinGw 를 사용하도록 launch.json 을 수정합니다. 또한, 매번 실행 마다 pretty printing 옵션을 넣도록 합니다.
4. 테스트 해봅니다.

## MinGw 설치
exe 로 되어 있는 mingw 설치 파일을 구할 수 있는 이<a href="http://mingw-w64.org/doku.php/download" target="_blank">링크</a>
로 이동합니다.

보통 google 에서 단순하게 MinGw 를 검색하면 이<a href="http://www.mingw.org/" target="_blank">링크</a> 가 제일 위에
뜰텐데, 여기 있는 디폴트 MinGw 에는 파이썬 모듈이 딸려있지 않습니다.

네, 사실 디버깅 할 때 vector 의 내부를 보여주는 기능은 python 의 pretty-print 라는 모듈입니다.
{% highlight python %}
import pprint
my_map = {'a':123, 'b':456}
pprint.pprint(my_map)
# 출력: {'a': 123, 'b': 456}
{% endhighlight %}
파이썬 모듈을 cpp 에 붙여서 쓰는 겁니다. 이상하다구요? 이상할 거 없습니다. python 자체가 C 로 만든 거니까요.

그러면 파이썬 기능이 장착되어 있는 MinGw 를 깔러 가봅시다. 
<a href="http://mingw-w64.org/doku.php/download" target="_blank">링크</a>

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp04.jpg){: .align-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp05.jpg){: .align-center}
동그라미 쳐진 것만 누르시면 됩니다.
{: .text-center }

exe 파일을 받았다면 실행합니다.
![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp06.jpg){: .align-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp07.jpg){: .align-center}
저는 x86_64 cpu 를 사용하기 때문에 Architecture 를 x86_64로 바꾸고 Next를 눌렀습니다.
{: .text-center }

설치가 끝나면 `C:\Program Files\mingw-w64` 경로에 폴더가 하나 생길 겁니다. 

대충 이런 이름입니다: `x86_64-7.2.0-posix-seh-rt_v5-rev0` 이 폴더 안에 MinGw 가 설치되어 있습니다.
그 안의 bin 폴더의 경로를 알면 되는데 

제 경우에는 
`C:\Program Files\mingw-w64\x86_64-7.2.0-posix-seh-rt_v5-rev1\mingw64\bin` 입니다.
여러분 컴퓨터의 실제 설치 경로를 찾아서 복사해두세요. 

설치는 이게 끝입니다! 간단하죠? 마우스 클릭 몇 번 누른게 다에요.

## tasks.json 수정

먼저 vs code 에서 cpp extension 과 code runner extension 이 설치되어 있는지 꼭! 확인하세요.
{: .notice--info}

vs code에서 tasks.json 을 수정합니다.
방금 설치한 MinGw 컴파일러의 경로를 지정해 주는게 다입니다.

수정할 항목은 `command` 랑 `options:cwd` 입니다. 제 경우에는 다음과 같습니다.

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp08.jpg){: .align-center}

```json
{
    // See https://go.microsoft.com/fwlink/?LinkId=733558 
    // for the documentation about the tasks.json format
    "version": "2.0.0",
    "tasks": [
        {
            "type": "shell",
            "label": "cpp.exe build active file",
            "command": "C:/Program Files/mingw-w64/x86_64-7.2.0-posix-seh-rt_v5-rev1/mingw64/bin/cpp.exe", // 여기!
            "args": [
                "-g",
                "${file}",
                "-o",
                "${fileDirname}\\${fileBasenameNoExtension}.exe"
            ],
            "options": {
                "cwd": "C:/Program Files/mingw-w64/x86_64-7.2.0-posix-seh-rt_v5-rev1/mingw64/bin" // 여기!
            },
            "problemMatcher": [
                "$gcc"
            ]
        }
    ]
}
```

tasks.json  수정 끝!

## launch.json 수정
역시 디버거 경로를 지정하면 됩니다.
그런데 한 가지 더 해야 할 일이 있습니다.

매 번 디버거를 실행할 때 마다. gdb에게 **pretty printing 기능을 사용하겠다** 라고 말해 줄 필요가 있습니다.
이를 위해서 `setupCommands` 값을 추가해 줍니다.

```json
{
    "version": "0.2.0",
    "configurations": [
        
        {
            "name": "(gdb) Launch",
            "type": "cppdbg",
            "request": "launch",
            "program": "${workspaceFolder}/${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": true,
            "MIMode": "gdb",
            "miDebuggerPath": "C:/Program Files/mingw-w64/x86_64-7.2.0-posix-seh-rt_v5-rev1/mingw64/bin/gdb.exe", // 경로지정
            "setupCommands": [ // 아래랑 똑같이 추가!
                {
                    "description": "Enable pretty-printing for gdb",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                }
            ]

        }
    ]
}
```

## 테스트
자 이제 준비는 끝났습니다.

실제로 디버깅이 잘 되는지 확인해 볼까요?
vector 에 요소를 추가하는 간단한 예제를 소개합니다.

{% highlight c++ %}
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> v;

    v.push_back(1);
    v.push_back(2);
    v.push_back(3);

    for (int i=0; i < v.size(); ++i) {
        cout<<v[i];
    }

}
{% endhighlight %}

원하는 지점에 breakpoint 를 넣고, <br>
`Ctrl + Shift + B` 로 빌드 <br>
`F5` 로 디버깅 시작! <br>

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp02.jpg){: .align-center}

![image-center]({{ site.baseurl }}/assets/images/2019-05-17-cpp03.jpg){: .align-center}
됬..다아
{: .text-center }

## 참고

* <a href="https://github.com/Microsoft/vscode-cpptools/issues/69" target="_blank">깃허브 이슈</a>
* <a href="https://stackoverflow.com/questions/4985414/how-to-enable-gdb-pretty-printing-for-c-stl-objects-in-eclipse-cdt/5713387" target="_blank">스택 오버플로우</a>
* <a href="https://code.visualstudio.com/docs/languages/cpp" target="_blank">vs code 문서</a>
* <a href="https://github.com/Microsoft/vscode-cpptools/blob/master/launch.md" target="_blank">기타</a>



