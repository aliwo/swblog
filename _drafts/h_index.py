from _drafts.random_test import random_list


def solution(citations):
    citations = sorted(citations)

    max_h = 0
    for i, elem in enumerate(citations):
        if elem <= len(citations) - i: # 얘는 왜 틀릴까? h가 h편 이상 인용된 논문 수 이하..
            max_h = elem
    return max_h

# 위는 틀린 답
# 아래는 맞는 답

def solution2(citations):
    citations = sorted(citations)

    for i, elem in enumerate(citations):
        # len(citations) - i 는 "h편 이상 인용된 논문 수" 이다.
        # h편 이상 인용된 논문 수가 h 이상 이라고 했으므로 elem > len(citations) 가 옳은 조건문.
        if elem >= len(citations) - i:
            return len(citations) - i
    return 0


while True:
    li = random_list(10, 0, 100)
    if solution(li) != solution2(li):
       print(li)
