---
layout: single
title:  "(파이썬으로 풀기) 카카오 블라인드 2018 프렌즈 4 블록 풀이"
date:   2020-01-16 11:10:03 +0900
categories: [python3, algorithm]
---


![image-center]({{ site.baseurl }}/assets/images/2020-01-16-kakao0.jpg){: .align-center}

## 문제
<a href="https://programmers.co.kr/learn/courses/30/lessons/17679" target="_blank">링크</a>


## 답안

{% highlight python %}
class G:
    pending = set()
    bombed = 0
    board = []


def bomb():
    for i, j in reversed(sorted(G.pending)):
        G.board[i].pop(j)
        G.bombed += 1
    G.pending = set()


def traverse(i, j):
    if j >= len(G.board[i+1]) - 1:
        return

    if G.board[i][j] == G.board[i][j+1] == G.board[i+1][j] == G.board[i+1][j+1]:
        for x, y in [(i + 1, j + 1), (i + 1, j), (i, j + 1), (i, j)]:
            G.pending.add((x, y))


def solution(m, n, board):
    G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
    
    while True:
        for i in range(len(G.board) - 1):
            for j in range(len(G.board[i]) - 1):
                traverse(i, j)
        if not G.pending:
            break
        bomb()

    return G.bombed
{% endhighlight %}

## 풀이
카카오판 애니팡을 시뮬레이션 하는 게임입니다. 다음 2가지 특성을 어떻게
구현할 것인지가 관건이라고 생각합니다.
* "블록이 밑으로 떨어져야 함"
* "2x2 블록들이 겹쳐져 있을 경우 같이 터져야 함"

먼저 블록이 떨어지는 것 부터 생각해 보겠습니다. 리스트 board 안에
맨 왼쪽 위 블록부터 순서대로 블록들이 나열되어 있습니다.

![image-center]({{ site.baseurl }}/assets/images/2020-01-16-kakao.jpg){: .align-center}

board 의 배치는 다음과 같습니다. `["TTTANT", "RRFACC", ...]` 
이제 board 의 배치를 90 도 틀어보겠습니다.

![image-center]({{ site.baseurl }}/assets/images/2020-01-16-kakao2.jpg){: .align-center}

즉 리스트 요소의 배치는 `["TTTANT", "RRFACC", ...]` 에서 -> `["TTTRRT", "MTRRRT", ...]` 이 됩니다.
리스트의 배치를 이와 같이 바꾸면 리스트에서 특정 요소를 pop() 했을 때 자동적으로 그 위의
블록들의 index 가 1 씩 내려가게 됩니다. 우리가 늘 사용했던 리스트의 기본 기능이죠.
**즉, 블록이 내려가는 기능을 직접 구현할 필요가 없습니다.**

{% highlight python %}
G.board = [[board[i][j] for i in reversed(range(m))] for j in range(n)]
{% endhighlight %}

이제 "2x2 블록들이 겹쳐져 있을 경우 같이 터져야 함" 부분을 살펴 보겠습니다.
2x2 블록을 발견했을 떄 바로 터뜨릴 수 있다면 문제가 하염없이 간단해 지겠지만
겹쳐있는 모든 2x2 블록을 모아서 한꺼번에 터뜨려야 합니다. 그러지 않으면 겹쳐있는 부분이
더 이상 2x2 가 아니게 되어 터지지 않게 됩니다.

![image-center]({{ site.baseurl }}/assets/images/2020-01-16-kakao3.jpg){: .align-center}

따라서 다음과 같은 전략을 사용하겠습니다.

1. board 를 순회하면서 2x2 블록을 모두 찾습니다. 찾을 때 마다 그 위치를 set 에 추가합니다.
    (리스트가 아니라 set 에 추가하는 이유는 중복을 피하기 위해서 입니다.)
2. board 를 처음 부터 끝까지 한 번 순회했다면, set 에 들어있는 모든 요소를 board 에서 pop 으로 제거합니다.
    (이때, 위 쪽에 있는 블록부터 pop() 해야 원치 않는 블록이 제거되는 것을 피할 수 있습니다.)
3. 한 번 순회했는데 조건에 부합하는 2x2 블록이 하나도 없었다면 반복을 멈춥니다.

코드로 구현하면 다음과 같습니다.

{% highlight python %}
    while True:
        for i in range(len(G.board) - 1):
            for j in range(len(G.board[i]) - 1):
                traverse(i, j)
        if not G.pending:
            break
        bomb()
{% endhighlight %}
traverse 는 조건에 부합하는 2x2 블록을 찾고, 찾았다면 set `G.pending` 에 추가하는 함수입니다. 
bomb 은 블록 폭파를 담당합니다.
