def solution(money, expected, actual):

    bat = 100
    for exp, act in zip(expected, actual):
        if money == 0:
            break
        money -= bat # 돈을 건다.
        if exp == act: # 딴다
            money += bat * 2
            bat = 100
        else: # 잃는다.
            bat = min(bat * 2, money)
        print(f'결과: {exp == act} {bat}  {money}')

    return money

# print(solution(1000, ['H', 'T', 'H', 'T', 'H', 'T', 'H'], ['T', 'T', 'H', 'H', 'T', 'T', 'H']))
# print(solution(1200, ['T', 'T', 'H', 'H', 'H']	, ['H', 'H', 'T', 'H', 'T']	))
print(solution(1500, ['H', 'H', 'H', 'T', 'H'], ['T', 'T', 'T', 'H', 'T']))
