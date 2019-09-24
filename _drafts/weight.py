
# https://programmers.co.kr/learn/courses/30/lessons/42886
# 저울

# 아... 가장 큰 weight 에 도달하기 전 까지 못 찾으면 오답이 되겠네
# 아님! i는 계속 증가하고, cur_sum 은 그대로 있으니까 정답이 나간다!

# 2019-09-21 오후 11시 42분 전부 정답이지만 효율성은 전부 실패하는 답안에 도달.

def solution(weight):
    weight.sort()

    i = 1 # 1 부터 increment 하는 답안 후보.
    j = -1 # 몇 번째 index 까지 cur_sum 을 만들었는지 저장하는 anchor
    cur_sum = 0

    while True: # weight 전체의 sum 을 구하는 것 보다 무한루프가 빠름

        for k in range(j+1, len(weight)): # j 가 len(weight) 를 벗어나면 for 문 동작 안함.
            if weight[k] <= i:
                cur_sum += weight[k]
                j = k
            else:
                break

        if cur_sum < i :
            return i

        i = cur_sum if cur_sum != i else i + 1


assert solution([3, 1, 6, 2, 7, 30, 1]) == 21
