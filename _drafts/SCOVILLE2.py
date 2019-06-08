# SCOVILLE 1 은 효율성 테스트에서 빵점을 받았습니다. 런타임 에러도 났구요.
# 그래서 힙을 사용해서 구현해 보겠습니다.

# K 는 최대 1,000,000,000 (10억) 이고, scoville 의 길이는 최대 1,000,000 (백만) 이므로
# 최악의 경우 백만번 연산하게 된다. (scoville 의 길이 만큼) C++ 은 1초 안에 1억번도 연산한다던데 파이썬은 백만에서 에러나는건가?
# 정확성 100%, 속도 0%

# 아니 진짜 sort 보다 heap 쓰는게 빠른거야?? 왜???
# -> 처음에 heap 으로 만드냐, sort 를 쓰느냐는 별 차이가 없다
# 하지만 음식을 섞는 과정에서 차이가 발생한다.
# 리스트의 경우, 0번째 요소를 2 번 삭제하기 때문에 벌써 2n
# 그리고 섞은 음식을 다시 넣을 때 정직하게 순회하면서 자리를 찾는다.
# 하지만 힙의 경우 삭제와 삽입 모두 log n 이다.

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] <= K:
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1

    if scoville[0] < K:
        return -1

    return answer



print(solution([1, 2, 3, 9, 10, 12], 7))
