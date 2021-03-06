---
layout: single
title:  "블루그린 배포(blue green deployment)"
date:   2019-03-03 16:10:03 +0900
categories: [regex]
--- 

## Preface
<a href="https://martinfowler.com/bliki/BlueGreenDeployment.html" target="_blank"> 
https://martinfowler.com/bliki/BlueGreenDeployment.html </a>
을 번역해 보았습니다. 

## BlueGreenDeployment
제 동료와 제가 고객들에게 강조하는 것들 중에 하나가, 완전히 자동화된 배포 프로세스 입니다.
배포를 자동화 하면 소프트웨어를 "완성" 하는 도중 불쑥 튀어나오는 마찰이나 지연
(frictions and delays, 크고 작은 문제들)들을 줄이는데에 도움이 됩니다.

Dave Farley 와 Jez Humble 이 이 주제에 관한 책 Continuous Delivery 를 거의 완성해 나가고 있습니다.
책은 Continuous Integration 과 관련된 많은 아이디어들을 기반으로 하는데, 소프트웨어를
빠르게 배포단계 까지 만드는 점 때문에 득세하고 있는 아이디어들입니다. 책에서 blue-green
development 에 대한 섹션이 눈에 들어왔는데, 충분히 활용되고 있지 않은 테크닉들이 보여서였습니다.
그래서 여기서 그 개념을 개략적으로 설명하려고 합니다.

배포를 자동화하기위해 해결해야 할 것들 중 하나가 바로 소프트웨어를 최종 테스트 단계에서
실제 배포 상태로 넘기는 일, 그 '넘어감'(cut-over) 자체입니다. 보통은 다운타임을 최소화 하기 위해서는
이 작업을 빨리 끝내야만 합니다. 블루 그린 배포는 가능한한 완전히 똑같은(identical)한
배포 환경 2개를 만들어 두는 방식으로 이 '넘김' 을 해결하려 합니다.

예를 들어 현재 blue 가 실제 운영되고 있다고 합시다. 소프트 웨어의 새 릴리즈를 준비할 때
최종 테스트를 green 환경에서 수행합니다. green 에서 소프트웨어가 제대로 동작하게 되면
라우터를 스위치 해서 모든 리퀘스트가 green 을 향하게 만듭니다. 이제 blue 는 놀게 되죠.

블루 그린 배포를 사용하면 롤백도 빠르게 할 수 있습니다. 만약 무언가가 잘못되었다면
다시 green 에서 blue 로 라우터를 스위치하는 것입니다. green 이 작동하는 동안 발생한
트렌젝션(blue 에는 없는)을 어떻게 할 것인가하는 문제가 여전히 남기는 하지만, 여러분이
어떻게 설계하느냐에 따라 blue green 양쪽 환경에 트렌젝션을 먹일 수 있습니다.
블루를 백업용으로 둔다거나, 혹은 '넘어갈' 때 어플리케이션을 읽기 전용 상태로 조금 두고 있다가
나중에 read-write 모드로 바꾸는 방식을 사용할 수도 있습니다. 이 방식으로 남은 상당한 이슈들
도 해결할 수 있습니다.  

두 환경(blue와 green)은 다르지만 최대한 똑같아야 합니다. 어떤 경우엔 두 환경이 서로 다른
하드웨어 위에서 돌아갈 수도 있고, 같은 하드웨어이지만 다른 가상 머신에서 돌아갈 수도 있습니다.
혹은 같은 OS 위에서 다른 IP 를 갖고 돌아갈 수도 있습니다. 

일단 green 환경을 배포한 뒤에 그 안정성이 만족할 만큼이라면, blue 환경은 다음 배포를 위해
staging 환경으로 둘 수 있습니다. 다음 릴리즈가 준비되었을 때 다시 green 에서 blue 로 바꾸
는 것이지요. 이런 방식으로 green 과 blue 환경이 주기적으로 돌아가면서 운영, 롤백, staging
을 맡습니다.

이 방식이 좋은 점이, 핫-스탠바이 가 필요할때 사용하는 매커니즘이랑 원칙적으로 같은
매커니즘이라는 것입니다. 따라서 매 릴리즈 때 마다 재앙-복구(disaster-recovery) 절차를
테스트 해보는 셈이죠.

근본적인 아이디어는 손쉽게 바꿔치기 할 수 있는 두개의 환경을 두는 것인데, 디테일로 들어가면
구현방식이 저마다 다릅니다. 라우터를 설정하는 대신에 
웹서버를 껐다 키는 방식으로 구현한 프로젝트도 있고, 같은 데이터베이스를 쓰는데 웹과 도메인
레벨에서 blue-green 스위치를 만드는 경우도 있습니다.

본 테크닉에서 데이터베이스가 꽤 까다로운 부분인데, 새 버전을 위해 schema 를 
수정해야 할때가 특히 그렇습니다. 비결은 schema 변경과 어플리케이션 업그레이드를
분리하는 겁니다. 먼저 구 버전과 새 버전의 서버를 모두 지원하도록 데이터베이스 schema 를 변경하고
모든게 제대로 작동하는지 확인한 뒤, 데이터베이스의 구 버전 지원을 끊어버리는 겁니다.

이 테크닉은 나온지가 꽤 되었습니다만, 실제 보여야할 만큼보다는 적게 눈에 띄는 것 같습니다. 


