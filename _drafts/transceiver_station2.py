from math import ceil

# 원형이 아니라는 점이 포인트. 문제가 쉬워짐.

def solution(n, stations, w):
    # 첫번째 아파트 ~ 첫번째 기지국
    cnt = max(ceil((stations[0] - w - 1) / (w * 2 + 1)), 0)

    # 첫번째 기지국 ~ 마지막 기지국
    i = 1
    while i < len(stations):
        cnt += max(ceil(((stations[i] - w - 1) - (stations[i-1] + w)) / (w * 2 + 1)), 0)
        i += 1

    # 마지막 기지국 ~ 마지막 아파트
    cnt += max(ceil((n - (stations[-1] + w)) / (w * 2 + 1)), 0)

    return cnt



# print(solution(11, [4, 11], 1)) # 3
# print(solution(11, [1, 11], 1)) # 3
# print(solution(11, [1, 10], 1)) # 3
# print(solution(11, [1, 8], 1)) # 3
print(solution(16, [9], 2)) # 3
# print(solution(17, [9], 2)) # 4

range
