test_case = int(input())

for i in range(0, test_case):
    days, pre_teams = [int(x) for x in input().split()]
    price_list = [int(x) for x in input().split()]

    minimum_average = sum(price_list[0:pre_teams]) / pre_teams # 아무거나 일단 지정

    for i in range(0, days):
        for j in range(i+pre_teams, days):
            cur_average = sum(price_list[i:j]) / (j-i)
            if minimum_average > cur_average:
                minimum_average = cur_average

    print(minimum_average)

# 위 답안은 시간 초과! 이중 for 문을 피해야 하거늘...
# 2019-04-24 김치와 비슷한 느낌이다. 나는 price_list 안의 내용은 랜덤 이라 모든 경우의 수를 다 계산해야 한다고 생각하지만
# 실제로는 계산하지 않고 피할 방법이 어딘가에 있는 모양이다.

# 한 가지 시도한 방법이 있는데, 스스로 틀렸다는 것을 증명해서 사용하지 않은 이론이다.
# pre_teams 가 3 이라고 할 때,
# 3일 동안 공연을 한다고 하고, 최소 평균을 갖는 부분 리스트 l 을 찾았다고 하자.
# 공연 일수를 3보다 더 늘린다고 하고 최소 평균을 갖는 부분 리스트 l2를 새로 찾는 다고 할 때, l2 는 반드시 l 을
# 포함한다는 것이다. 그러나 price_list 가 다음과 같고, pre_teams 가 2 라고 생각하면 본 가설이 틀렸다는 것을
# 금방 알 수 있다.
# price_list = [1, 10000, 50, 100, 20, 3, 40, 1]


