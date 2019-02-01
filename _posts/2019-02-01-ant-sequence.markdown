---
layout: single
title:  "알고리즘: 개미수열"
date:   2019-02-01 09:21:03 +0900
categories: [algorithm]
---



## 문제소개


개미수열은 다음과 같은 수열입니다. (이 수열은 소설 “개미”에서 소개되었기 때문에 개미 수열이라고 불립니다.)

1, 11, 12, 1121, 122111 .....

이 수열은 앞의 수의 연속된 같은 숫자를 묶어서 숫자와 그 개수를 읽는 방식으로 만들어집니다. 
•1을 “1이 한 개” 혹은 11로 읽습니다.
•11을 “1이 두 개” 혹은 12로 읽습니다.
•12를 “1이 한 개, 2가 한 개” 혹은 1121로 읽습니다.
•1121을 “1이 두 개, 2가 한 개, 1이 한 개” 혹은 122111로 읽습니다.
•이와 같은 방법으로 계속해서 다음 수를 만들어 갑니다.

입력으로 n 이 주어질 때 n번째 개미 수열을 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

제한사항
•n은 40이하의 자연수입니다.


## 입출력 예


입출력 예 #1 <br>
**2 11** <br>
 1, 11 ...로 두 번째인 11을 반환합니다.



입출력 예 #2 <br>
**5 122111** <br>
 1, 11, 12, 1121, 122111 ...로 다섯 번째인 122111을 반환합니다.

## 풀이

코드는 더럽지만 풀었다~


{% highlight python %}
def next_ant_seq(prev_seq):
    result = []
    target = prev_seq[0]
    cnt = 0
    for char in prev_seq:
        if char == target:
            cnt += 1
        else:
            result.append('{}{}'.format(target, cnt))
            target = char
            cnt = 1
    result.append('{}{}'.format(target, cnt))

    return ''.join(result)

def solution(A):
    answer = '1'
    for a in range(A-1):
        answer = next_ant_seq(answer)

    return answer
{% endhighlight %}
