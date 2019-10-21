import sys
sys.setrecursionlimit(99999999)

class G:
    left = []
    right = []
    cache = {}

def game(l, r):
    key = f'{l} {r}'
    if key in G.cache:
        return G.cache[key]

    # 기저 사례: 왼쪽이나 오른쪽 카드를 다 썼을 경우
    if l >= len(G.left) or r >= len(G.right):
        return 0

    a = 0
    for i in range(r, len(G.right)):
        if G.left[l] > G.right[i]:
            a += G.right[i]
        else:
            G.cache[key] = a + max(game(l + 1, i + 1), game(l + 1, i))
            return G.cache[key]

    # break 를 거치지 않고 전부 순회했을때의 예외처리를 꼭 하자.
    # break 를 거치지 않았을 때 game(l+1, i) 를 호출하면 오른쪽 마지막 카드를 2번 세개 된다.
    G.cache[key] = a
    return G.cache[key]



def solution(left, right):
    G.left, G.right = left, right
    return game(0, 0)


# 아래는 재귀를 사용하지 않는 반복 DP
def solution(left, right):
    dp = [[0 for x in range(len(left)+1)] for y in range(len(right)+1)]
    # dp 는 가로 세로가 left + 1 인 2중 배열
    # 맨 오른쪽 아래의 결과가 답이 된다.
    for i in range(1, len(left)+1):
        for j in range(1, len(right)+1):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) # 양쪽 다 버리는 경우 / 왼쪽만 버리는 경우
            if right[j-1] < left[i-1]:
                dp[i][j] = dp[i][j-1] + right[j-1] # 할당 했던걸 재할당?
    return dp[len(left)][len(right)]



print(solution([3, 2, 5], [2, 4, 1]))
# print(solution([3, 2, 5, 10], [2, 4, 1, 6]))
