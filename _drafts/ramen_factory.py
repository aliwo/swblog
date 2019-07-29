# 하루에 딱 1톤 만 밀가루를 사용한다.
# 밀가루를 제공받는 횟수는 최소로!
from _drafts.random_test import random_list
import traceback

def foresee(start_i, stock, dates, supplies):
    '''
    enduraable_days 가 빈 경우를 예외처리 합니다.

    현재 stock 을 갖고 며칠 까지 버틸 수 있는지를 조사 한 뒤,
    배급을 받아야 하는 날을 판단합니다.
    '''
    endurable_days = []

    if start_i == 0:
        start_day = 0
    else:
        start_day = dates[start_i - 1]

    if start_i == len(dates): # +1 을 하기 때문에 start_i 가 len(dates) 와 같아질 가능성이 존재.
        return start_i - 1

    for i in range(start_i, len(dates)): # 현재 stock 으로 며칠 까지 버틸 수 있는지 계산합니다.
        if stock - (dates[i] - start_day) >= 0: # TODO; endurable_days 가 비는 이유는 이것 밖에 없다.
            endurable_days.append(i)
        else: # break 가 없으면 시간 초과가 난다. 실패하는 테스트는 그대로 실패.
            break

    if not endurable_days:
        return 0

    max_i = endurable_days[0]
    for i in endurable_days:
        if supplies[i] > supplies[max_i]:
            max_i = i

    return max_i



def solution(stock, dates, supplies, k):
    answer = 0
    if stock >= k: # 예외처리: 처음 부터 k 일 까지 버틸 stock 이 남아있는 경우
        return 0

    # 예외처리를 통과했다면, 한 번 이상은 배급을 받아야 한다는 말입니다.
    today_i = foresee(0, stock, dates, supplies)
    stock = stock + supplies[today_i] - dates[today_i]
    answer += 1

    while stock < k - dates[today_i]: # k 까지 버틸 stock 이 생길 때 까지 계속합니다.
        lastday_i = today_i
        today_i = foresee(today_i+1, stock, dates, supplies)
        stock = stock - (dates[today_i] - dates[lastday_i]) + supplies[today_i]
        answer += 1

    return answer


assert solution(4, [4, 10, 15], [20, 5, 10], 30) == 2 # 예제, dates[1] 을 건너 뛰는 경우
assert solution(4, [4, 10, 29, 30], [6, 19, 1, 10], 30) == 3 # 매 번 밀가루를 겨우 맞추는 경우
assert solution(29, [29], [1], 30) == 1 # 마지막 날에 배급을 받는 경우
assert solution(31, [4, 10, 29, 30], [6, 19, 1, 10], 30) == 0 # 처음 stock 으로 끝 까지 버티는 경우
assert solution(4, [4, 10, 11, 15], [20, 5, 3 ,10], 30) == 2 # 2 번 건너 뛰는 경우
assert solution(4, [4, 10, 11, 15], [20, 5, 13 ,10], 30) == 2 # 배급 하고 한 번 뛰고, 다시 배급 하고 뛰기

assert solution(4, [4, 10, 10], [8, 4, 30], 30) == 2 # 리스트에 중복이 존재하는 경우

# 테스트 케이스 10 의 k 는 155 ! 찍어서 맞췄다... 그리고 dates 의 길이는 41개 이다.

# assert solution(4, [4, 10, 10], [8, 4, 30], 155)


while True:
    try:
        print(solution(3, [1, 3, 6, 8, 9, 10, 16, 20, 23, 29, # 0 ~ 9 , 10개
                           32, 37, 41, 44, 50, 53, 63, 72, 80, 83, # 10 ~ 19, 10개
                           90, 100, 102, 104, 105, 110, 112, 116, 117, 120, # 20 ~ 29, 10개, 20 은 100을 넘지 않음.
                           124, 127, 129, 130, 133, 135, 136, 138, 140, 141,# 30 ~ 39, 10개, 30은 100 초과임
                           150, 152# 40. 이것으로 41개
                           ], random_list(41, 1, 30), 155))
    except Exception as e:
        traceback.format_exc()


