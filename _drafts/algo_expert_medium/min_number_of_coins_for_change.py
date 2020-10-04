
strategy = '''
답지의 접근 방식:
배열 result[0] 에 주어진 denomination 으로 0원을 만들때의 minimum number of coins 를 저장한다.
result[1] 은 1원을 만들 때 의 minimum number of coins ...

자 이제 denoms 를 회전하면서
i 보다 denom 이 작을 때 (즉, i원을 만드는 데에 denom 을 사용할 수 있을 때)
result[i] = min(result[i], result[i - denom] + 1) # 현재 result[i] 값 혹은, denom 동전 하나를 써서 만들 수 있는 값 중 min 을 취한다.
모든 denoms 에 대해 위 과정을 반복한다.
'''

def minNumberOfCoinsForChange(n, denoms):
    result = [float('inf') for _ in range(n+1)] # result[n] 은 n이 n일 때의 정답(min_number_of_coins)
    result[0] = 0
    for denom in denoms:
        for i in range(len(result)):
            if denom <= i:
                result[i] = min(result[i], result[i - denom] + 1) # result[i - denom] 은
    return result[n] if result[n] != float('inf') else -1


# print(minNumberOfCoinsForChange(7, [1, 5, 10]))
# print(minNumberOfCoinsForChange(0, [1, 5, 10]))
# print(minNumberOfCoinsForChange(5, [2, 3, 4]))
# print(minNumberOfCoinsForChange(5, [2, 4]))
print(minNumberOfCoinsForChange(135, [130, 4, 1, 60, 75]))

