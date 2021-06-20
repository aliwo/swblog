# https://programmers.co.kr/learn/courses/30/lessons/42626

# 먼저 scoville 을 오름차순으로 정렬한다.

# 기저 사례: 기준치를 넘을 수 없는 경우... 는 어떻게 구할까? 다 섞어 봐야 하나?

# 문제를 쪼갠다. 항상 0번째 요소가 가장 작고, 1번째 요소가 그 다음으로 작도록


def insert(li, n):
    for i in range(len(li)):
        if li[i] > n:
            li.insert(i, n)
            return
    if i == len(li) - 1:
        li.append(n)


def mix(scoville):
    new_food = scoville[0] + scoville[1] * 2
    scoville._pop(0)
    scoville._pop(0)
    insert(scoville, new_food)


def solution(scoville, K):
    answer = 0
    scoville.sort()

    while scoville[0] <= K and len(scoville) > 1:
        mix(scoville)
        answer += 1

    if len(scoville) == 1: # 음식이 하나 남았는데 K 이상이 안 될 경우
        if scoville[0] < K:
            return -1


    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
