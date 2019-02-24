---
layout: single
title:  "premiere 2019 cc gpu 가속 사용하기"
date:   2019-02-17 22:10:03 +0900
categories: [premiere]
--- 

## 개요
premiere 설치 권장사항에 포함된 몇 개의 하이엔드 그래픽 카드를
제외하고는 프리미어 설치 이후에 'gpu 가속' 이 제대로 활성화가 안 되는 모양이다.

필자도 렌더러의 선택 박스가 비활성화 된 상태로, 'Mercury 재생 엔진 소프트웨어 전용' 으로 강제되어 있었다.

``
'Mercury 재생 엔진 소프트웨어 전용' 밖에 선택할 수 없다면, GPU 가속이 안 되고 있는 상황이다.
{: .text-center }

기껏 사서 끼워둔 그래픽 카드를 놀릴 수는 없다. GPU 가속을 활성화 시키는 방법을 알아보자.


## self test
이미 프로젝트를 생성한 상태에도 해당 프로젝트가 GPU 가속을 사용하는지 확인하는 방법이 있다.

파일 > 프로젝트 > 일반 탭을 선택해 대화상자를 연다.

대화 상자에서 '소프트 웨어 전용' 만 강제로 선택되어 있고, 다른 옵션으로 바꿀 수 없다면
현재 premiere 가 그래픽 카드를 제대로 인식하지 못하고 있다는 증거다. 


## 준비할 것
먼저 본인의 그래픽 카드 드라이버를 최신으로 업데이트 한다.

* <a href="https://www.nvidia.co.kr/Download/index.aspx?lang=kr" target="_blank">Nvidia 드라이버</a>
* <a href="https://www.amd.com/ko/support" target="_blank">Radeon 드라이버</a>

GPU 가속 (OpenCL 이든 CUDA 이든)을 사용하려면, 해당 가속 기능을 지원할 만큼 최신인
드라이버가 필수이다. 필자는 컴퓨터를 산 지 1년 남짓인데도 드라이버 업데이트를 안 해서
한 참 해맸었으므로 여러분은 꼭, 드라이버 업데이트를 먼저 해 두기를 권장한다.

## GPU sniffer

그래픽 카드 드라이버 업데이트가 완료되었다면, premiere 를 종료한 후,
premiere 설치 폴더로 이동한다. (윈도우라면 보통 C:\Program Files\Adobe\Adobe Premiere Pro CC 2019)
그 안에서 GPUsniffer 라는 응용 프로그램을 찾는다.

![image-center]({{ site.baseurl }}/assets/images/2019-02-20-gpu-sniffer.jpg){: .align-center}

실행한다.
{: .text-center }

프로그램을 실행하면 검은 화면(cmd 창) 이 뜨면서 뭔가 글자가 드르륵 지나가고
창이 바로 닫힌다. 정상이다. (드르륵 지나가는 글씨 사이에서 자신의 그래픽 카드 이름이 보인다면 성공인데,
창이 바로 닫혀 버리니 신경 쓸 거 없다.) 그 후 premiere 를 재실행한다.

## 확인

다음과 같이 CUDA (혹은 radeon 그래픽 카드라면 OpenCL) 선택지가 보이면 성공이다!

![image-center]({{ site.baseurl }}/assets/images/2019-02-20-cuda.jpg){: .align-center}



## 효능
그래픽 카드가 좋지 않아서 그런가 (1050 ti)
gpu 를 쓰긴 쓴다. 쓰는데 gpu 사용률은 5% 남짓으로 성능을 끌어내질 못하고 있었다.
뭔가 nvidia 쪽에서 설정을 더 해줘야 하는지? 는 잘 모르겠다...




