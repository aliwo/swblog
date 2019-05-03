# 19% 까지 갔다가 시간 초과 난 답

days, max_rest = [int(x) for x in input().split(' ')]
tempreatures = [int(x) for x in input().split(' ')]
kimchi_coef = [int(x) for x in input().split(' ')]
max = 0
coef_max = 0

for in_ in range(0, days):
    # prev_term = 0 # 김치 온도 항의 값은 0 부터 시작
    if kimchi_coef[in_] < coef_max: # max 장독대보다 더 작은 장독대값은 계산하지 않습니다.
        continue
    coef_max = kimchi_coef[in_]
    for out in range(in_, min(in_+max_rest+1, days)):
        cur_term = (out - in_) * tempreatures[out]
        # if prev_term > cur_term:
        #     break # 절벽 이후는 break
        cur_kimchi = cur_term + kimchi_coef[in_] # 김치 맛을 계산하는 김치 expression
        if max < cur_kimchi:
            max = cur_kimchi
        prev_term = cur_term

print(max)


# 절벽의 가정
# 온도가 현저히 떨어지는 '온도 절벽' 이 있다고 가정할 때,
# 절벽 이후의 경우의 수는 생각 할 필요가 없다.

