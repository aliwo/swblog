---
layout: single
title:  "ubuntu 에 python 3.7 혹은 3.6 설치하기"
date:   2019-03-07 16:10:03 +0900
categories: [linux, ubuntu]
--- 


```
attributeerror: module 'importlib._bootstrap' has no attribute 'sourcefileloader'
```

위에 보이는 에러 문구를 해결하기 위해 오신 모든 개발자 분들. 환영한다.

**주의:** 뒤늦게 ubuntu 14 에서는 python3.7 을 빌드할 떄 에러가 날 수 있다는 걸 알았습니다.
본 문서는 outdated 되었습니다... 나중에 ubuntu 16 으로 제대로 깔아보겠습니다. 
{: .notice--info}

## 발단
우분투(14 기준)는 기본적으로 python3이 python3.4 버전으로 깔려 있고,
같이 python2 도 깔려 있다.
파이썬 3 개발자가 늘 윈도우 노트북에서 하던 대로 무심코 
**python** 혹은 **pip** 명령어를 입력하게 되면
각각 python2 와 pip2 가 실행되는 기적을 보여준다.

필자가 리눅스 서버 운영을 입문할 당시에는
리눅스에서 가상환경을 처음 만들고 성공적으로 의존성을 모두 설치한 뒤
(flask 가 되었든 django가 되었든)
즐거운 마음으로 python run.py 를 실행하면 에러 폭탄이 떨어지는 걸 보곤 했다.

그나마 syntax error 는 쉽게 눈에 보인다. 그리고 콜 스택에서 python2가 보이기 때문에
자신이 파이썬2 를 실행해버리고 말았다는 걸 금방 알아챌 수 있었던 걸로 기억한다.
 
그러나 pip 에도 pip3 와 pip2 가 있다. 이 사실을 모르는 상태에서 연신 pip freeze 를 
연타한다면 멀쩡히 잘 설치된것 처럼 보여준다. (환각..) 

```
$ pip freeze
CherryPy==18.1.0
Click==7.0
Flask==1.0.2
Flask-API==1.1
google-api-python-client==1.7.8
... 후략
```
pip 曰 : "잘 설치 됬는 뎁쇼?"
{: .text-center}


모든 의존성이 pip2 에 설치되었다는 사실은 꿈에도 모르는채 개발자는 어리둥절해 지고 만다.

그리곤 구글에
"flask 를 분명히 설치했는데 flask 모듈이 없대요!!"
{: .text-center}

![image-center]({{ site.baseurl }}/assets/images/2019-03-07-hellllp.jpg){: .align-center}

를 검색해도 별 도움은 안 된다. 왜냐(킹냐 갓냐), 문제는 다른데에 있으니까.


## python 교통정리를 해보자.
이번 기회에 파이썬 3.7을 설치해야할 일이 생겨서 이 참에 리눅스 파이썬3.7
설치와 해당 파이썬 버전에 적합한 가상환경 설치를 진행해 보고자 한다.
침착하게 본 문서를 따라서 파이썬 3.7 을 설치한다면 이제 당신의 정신건강에도
청신호가 들어올 것이다.
 
## 결론
급한 여러분을 위해 결론 먼저 소개한다.

파이썬 3.7 설치용 bash 스크립트이다. 우분투 14 에서 파이썬 3.7 을 깔기 위해선 ppa 라는게
필요하다.
``` bash
#!/usr/bin/env bash
# 파이썬 3.7 설치
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.7

python3.7 --version
```

**별명짓기**

**/home/<사용자 이름>/.bash_aliases**

파이썬 3.7 이 곧 python 을 의미하도록 수정한다. 이제 제발 python2 는 놓아주도록 하자.
파일 명 .bash_aliases 를 사용자의 home 에 위치시킨 후, ssh 를 끊고 다시 접속한다.
``` bash
alias python=python3.7
alias pip=pip3
```
python2를 써야만 하는 정말 특별한 이유가 없다면
alias 를 지어두는게 정신 건강에 좋다. alias 없이 명령어를 실행하면 수 많은 에러를 맛 보게
될 수도 있다.

다음은 python3.7 용 venv 를 설치한 후, 실제로 가상환경을 하나 만들어 activate 한다.
``` bash
sudo apt install python3-pip
sudo apt install python3.7-venv
python -m venv venv
source venv/bin/activate
```

이제 `pip --version` 을 입력해본다.
```
$ pip --version
$ pip 10.0.1 from /home/ubuntu/streamer/venv/lib/python3.7/site-packages/pip (python 3.7)
```
꼭 끝에 **python 3.7** 이라고 떠야 한다.! 떴다면 성공! 이제 평소처럼
pip install 을 사용해서 의존성을 깔면 된다.


## 필요사항
다음의 사항을 준비, 혹은 숙지하고 있어야 한다.
* virtualenv 와 venv 는 서로 다른 것이다. (virtualenv 는 legacy)
* 본 포스트는 ubuntu 14 를 기준으로 한다.


## 주의
인터넷에 돌아다니는 파이썬 3.7 설치 문서중에
```
$ wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz
```
이렇게 tar.xz 소스파일을 직접 받아서 빌드를 권장하는 글이 있다.
본인의 리눅스 인스턴스가 극강의 성능을 자랑한다면 해 볼 만하지만,
싱글 코어 서버로는 정말 한나절이 걸리니 비추한다.
그리고 다음과 같은 에러도 뜬다.
```
./python -E -S -m sysconfig --generate-posix-vars ;\
        if test $? -ne 0 ; then \
                echo "generate-posix-vars failed" ; \
                rm -f ./pybuilddir.txt ; \
                exit 1 ; \
        fi
Fatal Python error: _PySys_BeginInit: can't initialize sys module

Current thread 0x00002ba95b277e00 (most recent call first):
Aborted (core dumped)
generate-posix-vars failed
make[1]: *** [pybuilddir.txt] Error 1
make[1]: Leaving directory `/home/ubuntu/tmps/Python-3.7.0'
make: *** [profile-opt] Error 2
(venv) ubuntu@dev1:~/tmps/Python-3.7.0$ 

```



## 참고
https://github.com/pypa/virtualenv/issues/1059

https://stackoverflow.com/questions/42558133/upgrading-python3-4-to-python3-6-on-ubuntu-breaks-pip/44354166#44354166

https://stackoverflow.com/questions/53070868/how-to-install-python3-7-and-create-a-virtualenv-with-pip-on-ubuntu-18-04

 
 






