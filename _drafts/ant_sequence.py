days, max_rest = [int(x) for x in input().split()]
tempreatures = input().split()
kimchi_coef = input().split() # input 을 int 로 바꾸는 시간 조차 아껴 보았다.
max = 0
coef_max = 0
max_first_value = 0 # 김치를 담그고 바로 다음 날 꺼낼 때의 김치 값을 저장합니다. max_first_value가 크다면 나머지는 비교할 필요 없음


for in_ in range(0, days):
    cur_coef = int(kimchi_coef[in_])

    if cur_coef < coef_max: # max 장독대보다 더 작은 장독대값은 계산하지 않습니다.
        continue
    coef_max = cur_coef

    # 테스트용 온도 계산
    test_temp = int(tempreatures[min(in_ + 1, days-1)])

    # 새로운 장독대를 시험해 볼때, 첫번째 온도 값을 비교
    cur_first_value = test_temp + cur_coef
    if cur_first_value < max_first_value:
        continue
    max_first_value = cur_first_value

    # 절벽 계산
    cliff = test_temp / max_rest

    for out in range(in_, min(in_+max_rest+1, days)):
        cur_temp = int(tempreatures[out])

        if cliff > cur_temp:
            break # 절벽 이후는 break

        cur_kimchi = (out - in_) * cur_temp + cur_coef # 김치 맛을 계산하는 김치 expression

        if max < cur_kimchi:
            max = cur_kimchi

print(max)


# 절벽의 가정
# 온도가 현저히 떨어지는 '온도 절벽' 이 있다고 가정할 때,
# 절벽 이후의 경우의 수는 생각 할 필요가 없다.

