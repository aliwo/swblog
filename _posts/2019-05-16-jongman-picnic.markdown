---
layout: single
title:  "피크닉"
date:   2019-05-16 11:10:03 +0900
categories: [algorithm]
--- 

## 문제
algospot의 PICNIC 을 풀어보았습니다.
<a href="https://algospot.com/judge/problem/read/PICNIC" target="_blank">PICNIC</a>

## Input 받기
각 케이스마다 문제를 한 번씩 실행하는 방식이 아니라
코드 실행 한 번에 여러 개의 케이스를 다 때려 박아야 하기 때문에
Input 받는 코드가 상당히 더럽습니다... 더 예쁜 방법이 있을 텐데... 저는 이렇게 했습니다.

{% highlight python %}
cases = int(input()) # case 의 수
results = [0] * cases # 결과값을 저장하는 전역변수
friends_dicts = [] # 친구 쌍을 저장하는 dict 의 리스트
for _ in range(cases):
    friends_dicts.append({}) # 빈 dict 생성
students = [0] * cases # 각 케이스별 학생의 수

for cur_case in range(cases):
    students[cur_case], _  = [int(x) for x in input().split()]

    for i in range(students[cur_case]):
        friends_dicts[cur_case][i] = []

    friends = input().split()
    for i, x in enumerate(friends):
        if i % 2 == 0:
            a, b = int(friends[i]), int(friends[i+1])
            if a > b: # a와 b 중 작은 값이 key 가 되고, 큰 값이 value 가 됩니다.
                friends_dicts[cur_case][b].append(a)
            else:
                friends_dicts[cur_case][a].append(b)
{% endhighlight %}

리스트 `results` 를 생성할 때에는 `results = [0] * cases` 를 사용했지만
리스트 `friends_dicts` 를 생성할 때에는  `friends_dicts = [{}] * cases` 를 사용하지 않는 데에는 이유가 있습니다.
<a href="https://stackoverflow.com/questions/56160509/python3-list-filled-with-empty-dict" target="_blank"> 참고</a>

결론만 얘기하자면 `friends_dicts = [{}] * cases` 를 사용하게 되면 리스트 안의 모든 
dict 가 같은 인스턴스가 되어 버리기 때문입니다. (정보를 따로 저장할 수 없다는 이야기입니다.)

input 받는 부분은 따로 설명할 것은 없고,
friends_dict 의 형성에 대해서 설명하겠습니다.

## friends_dict 의 형성

{% highlight python %}
for cur_case in range(cases):
    students[cur_case], _  = [int(x) for x in input().split()]

    for i in range(students[cur_case]):
        friends_dicts[cur_case][i] = []

    friends = input().split()
    for i, x in enumerate(friends):
        if i % 2 == 0:
            a, b = int(friends[i]), int(friends[i+1])
            if a > b: # a와 b 중 작은 값이 key 가 되고, 큰 값이 value 가 됩니다.
                friends_dicts[cur_case][b].append(a)
            else:
                friends_dicts[cur_case][a].append(b)
{% endhighlight %}
반 멤버가 0, 1, 2, 3 으로 총 4명이고, 모두가 친구라고 하면 결과값 dict 는 다음과 같은 모양입니다.
{% highlight python %}
{
    0: [1, 2, 3],
    1: [2, 3],
    2: [3],
    3: [],
}
{% endhighlight %}
dict 의 의미는 다음과 같습니다.

0과 1, 2, 3 은 친구다.

1과 2, 3 은 친구다.

2과 3 은 친구다.


**왜 작은 값이 key가 되고 큰 값이 value 가 되죠?** <br>
취향입니다, 뒤에 짝을 지어주는 함수 findCombination() 의 구현을 보게 되면
항상 아직 짝이 없는 친구중 0번째 친구를 짝 지어주기로 하는데, 구현이 이렇게 되면
작은 번호의 친구를 우선으로 dict에 적어주어야 하기 때문입니다.
반대로 아직 짝이 없는 친구중 마지막 번 친구를 먼저 짝 지어주기로 한다면
큰 값을 key로 해도 됩니다.
{: .notice--info}



## Insight: 친구사전과 친구 리스트의 차이 
친구 여부를 저장하는 자료구조 후보로 2가지를 생각해 볼 수 있는데
* 친구사전 `{0:[1,2,3] ...}`
* 친구 튜플의 리스트 `[(0,1), (0,2), (3,0) ...]`

친구 사전의 형태를 취할 경우에
멤버 n 의 친구를 찾기 위해서 리스트 전체를 순회할 필요가 없습니다. 친구_사전[n] 으로 n의
친구들을 바로 알 수 있다는 장점이 있습니다.

그래서 친구 사전을 택했구요. 이제 친구사전을 이용해서 짝을 지어줘 봅시다.

## 짝짓기: findCombination()
{% highlight python %}
def findCombination(left_behind):

    if len(left_behind) == 0: # 기저 사례 1: 모든 친구를 짝 지은 경우
        results[cur_case] += 1
        return

    # left_behind 중 0 번째 멤버를 짝 지어줄 방법을 찾는다.
    for elem in friends_dicts[cur_case][left_behind[0]]:
        if elem in left_behind:
            new_left_behind = left_behind[1:]
            new_left_behind.remove(elem)
            findCombination(new_left_behind)
{% endhighlight %}

함수 findCombination 에 들어가는 변수 left_behind 는 짝 없이 남겨진 친구들을
의미합니다. 맨 처음에 findCombination 을 실행할 때 left_behind 는 모든 친구들이 담겨진 리스트입니다.

실행 후, if 문을 건너서 for 문에 들어가게 되면, left_behind 에 남아있는 친구들 중 0번째
친구에게 짝을 지어주게 됩니다. 친구_사전[0] 으로 0의 친구들을 찾아주죠.

0번의 친구를 찾을 때 다음과 같은 경우의 수를 고려해 볼 수 있습니다.
* 0번은 외톨이: 0번은 친구가 없습니다. 이 경우 더 이상 재귀호출이 발생하지 않으므로
가능한 조합의 수는 0입니다. 
* 0번은 친구가 한 명: for 문은 한 번 회전 하고 끝납니다. 
* 0번은 친구가 많다: for 문이 여러번 회전 하는데, findCombination 을 호출할 때
 주의할 점이 있습니다. 기존의 left_behind 를 수정하면 안됩니다.
 항상 **새로운 left_behind**를 생성해서 넘겨주어야 한다는 것입니다.
 0번과, 0번의 친구 A 를 짝 지어주었다면, left_behind 에서 0번과 A 를 제외한 새로운 new_left_behind
 를 생성해서 findCombination()을 재귀호출 합니다. 만약 새로운 left_behind 를 생성하지 않고 
 기존 left_behind 에 손을 대었다면 for 문 실행 도중 left_behind 가 오염되게 되고, 다음 번
 findCombination() 을 호출할 때 예상과 다른 답이 나오게 됩니다.
 
findCombination() 의 재귀 호출 중, left_behind 가 비게 되면 if 문을 통해 재귀호출이
종료됩니다. 출력할 결과에 +1 을 하고 return 합니다.

 
## 실행 예제

친구가 4명 (0, 1, 2, 3) 이고
모두가 서로 친구일 때 정답은 `3` 입니다. 
* (01) (23)
* (02) (13)
* (03) (12)

프로그램은 다음의 순서대로 실행합니다.
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="693px" height="333px" viewBox="-0.5 -0.5 693 333" content="&lt;mxfile modified=&quot;2019-05-16T04:28:56.032Z&quot; host=&quot;www.draw.io&quot; agent=&quot;Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0&quot; etag=&quot;crP2hGOVSw-Ve8jGydS0&quot; version=&quot;10.6.7&quot; type=&quot;device&quot;&gt;&lt;diagram id=&quot;6a731a19-8d31-9384-78a2-239565b7b9f0&quot; name=&quot;Page-1&quot;&gt;7ZpLk6M2EIB/DVXJIS4kgYDjGHtmD7tVSaaSnT1tyVgG7crIpZFf+fURIJ62J57x2B6n4GK6JXXr8TVSgy0UzjcPkiySL2JKuQXt6cZCIwtCADDUP5lmW2iwgwpFLNnUVKoVj+wfapS20S7ZlD63KiohuGKLtjISaUoj1dIRKcW6XW0meNvrgsR0R/EYEb6r/cqmKqnGFdQFnyiLE+Pah15RMCHRz1iKZWr8WRDN8qsonpPSlhnoc0KmYt1QobGFQimEKu7mm5DybG7LaSva3R8orfotaaqOauC5picrwpe07HTeNbUtp4NO9ewYMRWp/hnmY6SZFaClH8v5olMhUXNuSqtB2lrgZEL5sJqmUHAh61bPikh1l61gR3fPODcWflCltoYZslRCq4RUiYhFSvhnIRalWyXFT1o60Csx9l3swKqkXFmkNTORqnsyZzwD9hPlK6pYREyB8QUcIzdM3udXZnJBIpbGWuuWrcx8ZF2Z6d43Wk1siijW+t3lMiv4LJYyotUamejRExFTVWlxoc1Wp9HYLPQDFXOq5FZXkJQTxVZttokJkbiqV2OibwwpB6kBPTU3So17RWpgT82NUuNckRq0hxrMdd+GU7bSt3F2a41Dyx9ad441HlkBtvygrKQ9NOvtNuV0pr5PaML0rq33y8yDbblDvTGGegCh9hYiyx2VLSeya6vroYN0m991whR91EuYla71+ekEgJvQtZQt3tpA0JLMkzkknMWp1kWaKCr/E0wiI2PV09KCSqZhoPKxagRfonRFpaKbF9krSwNzpDGHT+SbjXLdOMp55jGYNE5x2H4XXJ1jcJ2xbDnnE5bqcBHpL78eTWsG+p1nBTml6M6wCl8F6LEhkOGv7/5H9M9sn/rgwvTbF6Tf8br0w4G7y3957D8D/+41+Adn4R/2/N86/9CxL0o/vgb9rwP0lU//120tPf0fiX4XXJB++jSK/97CvyD982H1R/jNXsfgN+D5/Rum9yDubVkf3TD1ZOpk99+yIQ5cI402ZsS5sDXC3lTvmNTROTEnNE1/F0z7qZhGHh4EjctvEe5AZ+BDP/BAgCEG2Edt+0UXjcnmm9COFw+1I8cBHUNFQrxjKA+KarAnxcm+d2oXSBzyhzw4zxbSbx2X3Dp29ok9QXtw6+gGwIUTh0NBse+V4QWyieLk0wdFHxTXyyYOhcRVEmxk9onzvGjqQ+JmQ+JDpBj7su4+xfi4KYZmTW6fmkKjVSbWzXLp5NTEANL8qvXi4/X9sxgXD1ykw8W3seMCDNrZhuu/LW1xfHcQYM9zQIBcx0deJzY7Zs+fxHh9JN5UJB4fUcfEDjxL7GBoDwCurzbkEAcDH9WX+7ZIwp3PhtCz3yl2tFj/o6uoXv9tDo3/BQ==&lt;/diagram&gt;&lt;/mxfile&gt;"><defs/><g><path d="M 157.53 209 L 277.8 264.75" fill="none" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 283.92 267.59 L 273.87 267.89 L 277.8 264.75 L 277.65 259.72 Z" fill="#e85642" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 147.13 145 L 288.5 67.84" fill="none" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 294.43 64.61 L 288.68 72.87 L 288.5 67.84 L 284.37 64.97 Z" fill="#e85642" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 178 175.83 L 268.9 174.64" fill="none" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 275.65 174.55 L 266.71 179.17 L 268.9 174.64 L 266.59 170.17 Z" fill="#e85642" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><rect x="1" y="147" width="175" height="60" rx="4.2" ry="4.2" fill="#e85642" stroke="none" pointer-events="none"/><g transform="translate(13.5,158.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="150" height="32" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 151px; white-space: nowrap; overflow-wrap: normal; font-weight: bold; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>실행</div><div>left_behind = [0,1,2,3]<br /></div></div></div></foreignObject><text x="75" y="23" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica" font-weight="bold">&lt;div&gt;실행&lt;/div&gt;&lt;div&gt;left_behind = [0,1,2,3]&lt;br&gt;&lt;/div&gt;</text></switch></g><rect x="281" y="143.5" width="150" height="60" rx="4.2" ry="4.2" fill="#f08e81" stroke="none" pointer-events="none"/><g transform="translate(296.5,147.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="118" height="48" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 119px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>findCombination()</div><div>짝 : [02]<br /></div><div>left_behind = [1, 3]<br /></div></div></div></foreignObject><text x="59" y="31" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><rect x="281" y="1" width="150" height="60" rx="4.2" ry="4.2" fill="#f08e81" stroke="none" pointer-events="none"/><g transform="translate(296.5,4.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="118" height="48" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 119px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>findCombination()</div><div>짝 : [01]<br /></div><div>left_behind = [2, 3]<br /></div></div></div></foreignObject><text x="59" y="31" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><rect x="281" y="271" width="150" height="60" rx="4.2" ry="4.2" fill="#f08e81" stroke="none" pointer-events="none"/><g transform="translate(296.5,274.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="118" height="48" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 119px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>findCombination()</div><div>짝 : [03]<br /></div><div>left_behind = [1, 2]<br /></div></div></div></foreignObject><text x="59" y="31" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><path d="M 433.17 173.83 L 530.9 173.98" fill="none" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 537.65 173.99 L 528.64 178.48 L 530.9 173.98 L 528.65 169.48 Z" fill="#e85642" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><rect x="541" y="143.5" width="150" height="60" rx="4.2" ry="4.2" fill="#f08e81" stroke="none" pointer-events="none"/><g transform="translate(559.5,147.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="112" height="48" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 113px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>findCombination()</div><div>짝 : [02, 13]<br /></div><div>left_behind = []<br /></div></div></div></foreignObject><text x="56" y="31" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><rect x="541" y="1" width="150" height="60" rx="4.2" ry="4.2" fill="#f08e81" stroke="none" pointer-events="none"/><g transform="translate(559.5,4.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="112" height="48" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 113px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>findCombination()</div><div>짝 : [01, 23]<br /></div><div>left_behind = []<br /></div></div></div></foreignObject><text x="56" y="31" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><rect x="541" y="271" width="150" height="60" rx="4.2" ry="4.2" fill="#f08e81" stroke="none" pointer-events="none"/><g transform="translate(559.5,274.5)"><switch><foreignObject style="overflow:visible;" pointer-events="all" width="112" height="48" requiredFeatures="http://www.w3.org/TR/SVG11/feature#Extensibility"><div xmlns="http://www.w3.org/1999/xhtml" style="display: inline-block; font-size: 14px; font-family: Helvetica; color: rgb(255, 255, 255); line-height: 1.2; vertical-align: top; width: 113px; white-space: nowrap; overflow-wrap: normal; text-align: center;"><div xmlns="http://www.w3.org/1999/xhtml" style="display:inline-block;text-align:inherit;text-decoration:inherit;"><div>findCombination()</div><div>짝 : [03, 12]<br /></div><div>left_behind = []<br /></div></div></div></foreignObject><text x="56" y="31" fill="#FFFFFF" text-anchor="middle" font-size="14px" font-family="Helvetica">[Not supported by viewer]</text></switch></g><path d="M 433.17 301.33 L 528.9 301.33" fill="none" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 535.65 301.33 L 526.65 305.83 L 528.9 301.33 L 526.65 296.83 Z" fill="#e85642" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 431.17 30.83 L 528.9 30.92" fill="none" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/><path d="M 535.65 30.93 L 526.64 35.42 L 528.9 30.92 L 526.65 26.42 Z" fill="#e85642" stroke="#e85642" stroke-width="3" stroke-miterlimit="10" pointer-events="none"/></g></svg>
 
## full code
{% highlight python %}
def findCombination(left_behind):

    if len(left_behind) == 0: # 기저 사례 1: 모든 친구를 짝 지은 경우
        results[cur_case] += 1
        return

    # left_behind 중 0 번째 멤버를 짝 지어줄 방법을 찾는다.
    for elem in friends_dicts[cur_case][left_behind[0]]:
        if elem in left_behind:
            new_left_behind = left_behind[1:]
            new_left_behind.remove(elem)
            findCombination(new_left_behind)


cases = int(input()) # case 의 수
results = [0] * cases # 결과값을 저장하는 전역변수
friends_dicts = [] # 친구 쌍을 저장하는 dict 의 리스트
for _ in range(cases):
    friends_dicts.append({}) # 빈 dict 생성
students = [0] * cases # 각 케이스별 학생의 수

for cur_case in range(cases):
    students[cur_case], _  = [int(x) for x in input().split()]

    for i in range(students[cur_case]):
        friends_dicts[cur_case][i] = [] # 모든 dict 가 한꺼번에 움직인다. 마치 같은 객체인것 처럼.

    friends = input().split()
    for i, x in enumerate(friends):
        if i % 2 == 0:
            a, b = int(friends[i]), int(friends[i+1])
            if a > b:
                friends_dicts[cur_case][b].append(a)
            else:
                friends_dicts[cur_case][a].append(b)


for cur_case in range(cases):
    findCombination(list(range(students[cur_case])))
    print(results[cur_case])
 
{% endhighlight %}


  
