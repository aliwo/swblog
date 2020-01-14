
'''
정확성  테스트
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.06ms, 10.7MB)
테스트 3 〉	통과 (0.06ms, 10.8MB)
테스트 4 〉	통과 (0.06ms, 10.7MB)
테스트 5 〉	통과 (0.07ms, 10.9MB)
테스트 6 〉	통과 (1.00ms, 10.9MB)
테스트 7 〉	통과 (9.66ms, 11.7MB)
테스트 8 〉	통과 (20.30ms, 11.8MB)
테스트 9 〉	통과 (20.98ms, 11.9MB)
테스트 10 〉	통과 (13.11ms, 11.5MB)
테스트 11 〉	통과 (0.06ms, 10.7MB)
테스트 12 〉	통과 (932.14ms, 26.1MB)
효율성  테스트
테스트 1 〉	통과 (2850.20ms, 37.7MB)
테스트 2 〉	통과 (3329.18ms, 39.4MB)
테스트 3 〉	통과 (3469.22ms, 40.2MB)
테스트 4 〉	통과 (2970.46ms, 37.6MB)
테스트 5 〉	통과 (3330.17ms, 40.2MB)
'''

def prune(window):
    cache = {}
    for elem in window:
        if elem[0] in cache:
            if elem[1] > cache[elem[0]]:
                cache[elem[0]] = elem[1]
        else:
            cache[elem[0]] = elem[1]

    return [(key, value) for key, value in cache.items()]


def solution(K, travel):
    '''
    이지선다를 반복하므로
    윈도우 크기가 계속 2배씩 증가하는 방식으로 계속 새로운 윈도우를 덮어 쓰면 된다.
    window 에는 바로 전 도시까지의 모든 경우의 수에 대해 (남은 K, 누적 모금액) 을 저장한다.
    각 단계마다 window 를 솎아 낼 수 있을까? 남은 시간이 같다면 모금액이 큰 값만 남기면 되잖아

    절대 우위를 사용한 최적화는 없어도 통과 된다 ^^
    남은 시간이 겹치는 경우를 이용한 최적화만 있으면 통과!
    왜 남은시간이 겹치는 경우가 많은 걸까?
    '''
    window = [(K - travel[0][0], travel[0][1]), (K - travel[0][2], travel[0][3])]

    for i in range(1, len(travel)):
        # 도보가 절대 우위인 경우
        if travel[i][0] < travel[i][2] and travel[i][1] > travel[i][3]:
            window = prune([(elem[0] - travel[i][0], elem[1] + travel[i][1]) for elem in window if elem[0] >= travel[i][0]])
            continue
        # 자전거가 절대 우위인 경우
        if travel[i][2] < travel[i][0] and travel[i][3] > travel[i][1]:
            window = prune([(elem[0] - travel[i][2], elem[1] + travel[i][3]) for elem in window if elem[0] >= travel[i][2]])
            continue

        # 절대 우위가 없는 경우
        new_window = []
        for elem in window:
            if elem[0] >= travel[i][0]:
                new_window.append((elem[0] - travel[i][0], elem[1] + travel[i][1]))
            if elem[0] >= travel[i][2]:
                new_window.append((elem[0] - travel[i][2], elem[1] + travel[i][3]))
        window = prune(new_window)

    return max([x[1] for x in window])


# assert solution(1650, [[500, 200, 200, 100], [800, 370, 300, 120], [700, 250, 300, 90]]) == 660
assert solution(3000, [[1000, 2000, 300, 700], [1100, 1900, 400, 900], [900, 1800, 400, 700], [1200, 2300, 500, 1200]]) == 5900
assert solution(100, [[1, 1, 1, 1], [99, 1000, 1, 1], [1, 1, 1, 1]]) == 3
