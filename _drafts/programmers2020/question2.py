from itertools import chain

def solution(n):
    memo = {i: {'head':[], 'mid': [], 'tail':[], 'len': 0} for i in range(1, n+1)}
    cur = 1
    num = 1
    memo[1]['head'].append(1)
    memo[1]['len'] = 1

    while num < n*(n+1)//2:

        # down
        while cur+1 in memo and memo[cur+1]['len'] < cur+1: # 다 채워지지 않으면 내려가서 채운다.
            cur += 1
            num += 1
            memo[cur]['head'].append(num)
            memo[cur]['len'] += 1

        while cur in memo and memo[cur]['len'] < cur:  # 다 채워지지 않으면 내려가서 채운다.
            num += 1
            memo[cur]['mid'].append(num)
            memo[cur]['len'] += 1

        # up
        while cur - 1 in memo and memo[cur - 1]['len'] < cur - 1:  # 다 채워지지 않으면 올라가서 채운다.
            cur -= 1
            num += 1
            memo[cur]['tail'].append(num)
            memo[cur]['len'] += 1


    result = []
    for key, val in memo.items():
        result = chain(result, chain(val['head'], val['mid'], reversed(val['tail'])))

    return list(result)




# print(solution(1))
# print(solution(2))
# print(solution(3))
# print(solution(4)) # [1,2,9,3,10,8,4,5,6,7]
# print(solution(5)) # [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]



