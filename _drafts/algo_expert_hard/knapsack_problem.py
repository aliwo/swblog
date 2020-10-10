from collections import defaultdict


def knapsackProblem(items, capacity):
    '''
    row 는 item
    col 은 knapsack 의 크기인 이차원 리스트를 생성
    '''
    memo = [[0 for _ in range(capacity+1)] for _ in range(len(items) + 1)]
    items.insert(0, None)
    elems = []

    for i in range(1, len(memo)):
        for j in range(len(memo[i])):
            if items[i][1] > j:
                memo[i][j] = memo[i-1][j]
                continue
            memo[i][j] = max(memo[i-1][j], memo[i-1][j-items[i][1]] + items[i][0])

    while i > 0 and j >= 0:
        if memo[i][j] != memo[i-1][j]:
            elems.append(i-1)
            j -= items[i][1]
        i -= 1

    return [memo[-1][-1], elems]



print(knapsackProblem([[1, 2], [4, 3], [5, 6], [6, 7]], 10))





