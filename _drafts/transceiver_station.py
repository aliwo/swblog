# 원형이 아니라는 점이 포인트. 문제가 쉬워짐.

def solution(n, stations, w):
    # field 생성
    field = [False for _ in range(n+1)]
    field[0] = True
    for station in stations:
        for i in range(max(1, station-w), min(station+w, n)+1):
            field[i] = True

    # 문제 풀이
    cnt = 0
    i = 1
    while i <= n:
        if field[i] == False:
            i = i + (2*w + 1)
            cnt += 1
            continue
        i += 1
    return cnt

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
print(solution(17, [9], 2))

