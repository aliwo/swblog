class G:
    memo = {}

def no_adj_sum(array, cur, i):
    anchor = f'{cur},{i}'
    if anchor in G.memo:
        return G.memo[anchor]
    if i >= len(array):
        return cur
    cur = cur + array[i]
    G.memo[anchor] = max(no_adj_sum(array, cur, i + 2), no_adj_sum(array, cur, i + 3))
    return G.memo[anchor]


def maxSubsetSumNoAdjacent(array):
    G.memo = {}
    return max(no_adj_sum(array, 0, 0), no_adj_sum(array, 0, 1))


