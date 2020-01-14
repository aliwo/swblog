from collections import Counter


'''
걸리는 시간이 오래 걸렸을 때 오답을 내는 경향이 있는 것 같다.
내가 생각하지 모한 부분은 어디인가.

현재 틀리는 케이스:
1, 6, 10, 11, 12, 15, 17, 18, 28, 30, 31, 및 효율성 테스트 전부

실제 답이 -1 인 케이스: 16, 19, 20, 23

본 함수가 -1 을 리턴하는 케이스:
15, 16, 17, 18, 19, 20, 23, 28, 30, 31, 효율성 2

즉, 답이 -1 이 아닌데 -1을 리턴해버리는 오답이 존재. (물론 다른 오답도 존재 ^^)
'''

def find_left_food(food_times, start, last_key):
    '''
    남은 음식이 존재할 때만 호출해야 합니다.
    '''
    while True:
        if food_times[start] > last_key:
            break
        start += 1
    return start

def solution(food_times, k):
    '''
    k 는 방송이 터지기 까지 남은 시간...
    리스트를 계속 회전하는 대신, counter 를 만들어서 회전하면 훨씬 빠르다.
    '''
    food_left = len(food_times)
    counter = Counter(food_times)
    last_key = 0

    for key in sorted(counter.keys()):
        # k 가 음수가 되는 경우는 말이 안되는 건가?
        k -= food_left * (key - last_key)
        food_left -= counter[key]
        last_key = key
        if food_left <= 0: # 방송이 끊기기도 전에 다 먹은 경우
            return -1
        if k < food_left:
            # 남아있는 음식을 세서 다음 먹어야 할 음식을 리턴
            i = 0 # 먹은 음식 수
            j = find_left_food(food_times, 0, last_key) # 다음 번 먹어야 할 음식의 인덱스
            while i < k:
                i += 1
                j = find_left_food(food_times, j+1, last_key)
            return j + 1


assert solution([10, 7, 6, 5, 5, 3, 2], 24) == 5
assert solution([2, 3, 10, 7, 6, 5, 5], 24) == 7
assert solution([3, 1, 2], 5) == 1
assert solution([3, 1, 2], 7) == -1

