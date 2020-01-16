---
title:  "객체지향"
date:   2019-09-14 09:21:03 +0900
---

## 추상화
추상화는 `특징을 뽑아내는 것` 을 말한다. 이렇게만 말하면 추상화가 어떻게 프로그래밍과
관련이 있는지도, 추상화를 어떻게 하는지도 알 수가 없으므로 먼저 비유를 든다.

미술 시간에 학교 운동장에 있는 나무를 보고, 그 나무를 도화지에 그린다고 생각해 보자.
나무를 그린다는 것은 나무가 가진 특성을 도화지 안으로 옮기는 것이다. 여기서 그 특성은
'모양'과 '색깔' 이다. 갈색 나무 줄기, 초록색 이파리, 줄기는 수직이고, 잎은 동그랗다.

한 편, 우리가 나무의 모양과 색깔을 도화지 안으로 옮길 수 있었던 것과 달리
나무의 경도, 나무의 생명력, 나무 열매의 달콤함 등은 도화지 안으로 옮기기 어렵다.

이처럼 추상화는 대상의 어떤 특성은 뽑아 내고, 어떤 특성은 무시한다.

추상화를 하다보면 서로 다른 대상간의 공통점을 발견할 수 있다. 예를 들어
강아지와 사람을 추상화 해 보자.

강아지의 특성: 짖는다. 숨쉰다. 먹는다. 
사람의 특성: 말한다. 숨쉰다. 먹는다.

강아지는 짖고, 사람은 말을 하지만 이 둘은 공통적으로 숨도 쉬고, 음식도 먹는다.
그렇다면 '숨쉰다' 와 '먹는다' 라는 특성을 합쳐서, `숨도 쉬고 음식도 먹을 수 있으면 동물이다.`
라고 정의해 볼 수 있을 것이다.

방금 '동물' 이라는 추상화 계층을 하나 만든 것이다. 
이제 '고양이' 라는 새로운 대상을 등장시켜보자. 고양이의 특성을 관찰한다.

고양이의 특성: 운다.(meow), 숨쉰다. 먹는다.

여기서 질문. 고양이는 우리가 정의한 추상화 계층 '동물'에 들어갈까?
들어간다. 숨도 쉬고, 음식도 먹기 때문.

정리하자면  

* 추상화는 대상으로 부터 '특징'을 뽑아내는 작업이다.
* 추상화를 통해 서로 다른 대상으로부터 공통점을 묶을 수 있다.



## 캡슐화
말 그대로 알약 캡슐을 생각하면 된다. 캡슐이 수행하는 기능은 다음과  같다.
* 약가루를 한 데 모아 준다.
* 약이 내부적으로 무슨 기능을 하는지 알 지 못해도, 약을 사용(그냥 먹으면)할 수 있게 해준다.
* 캡슐 내부의 약가루와 외부를 차단한다.

*접근제어*






## 다형성 




## 상속

