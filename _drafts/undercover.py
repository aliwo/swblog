from collections import defaultdict

def solution(clothes):
    answer = 0
    cache = defaultdict(lambda: [])

    for cloth in clothes:
        cache[cloth[1]].append(cloth[0])

    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

