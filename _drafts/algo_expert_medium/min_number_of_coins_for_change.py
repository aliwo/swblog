
strategy = '''
항상 가장 큰 수를 취할 수 있는 건 아니다.
n = 5 이고
denoms = [2, 3, 4]
일때, 4를 쓸 수는 없다. 2랑 3을 써야 답에 다다른다. 그래서 dp를 써야 하는 것 

n 이 0일 떄 1가지 방법 (안 내는 것)
n 이 1일 때 1가지 방법 (1을 내는 것) 호은  -1
n 이 2일 때 

가장 큰 수를 넣고, 뻗어 나가다가 전부 실패하면
그 다음 수를 넣고 뻗어 나가는 것.

제일 큰 수를 쓴다고 제일 적은 횟수를 쓰는게 아니다.
n: 135, denoms: [130, 4, 1, 60, 75]
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

