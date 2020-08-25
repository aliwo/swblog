# class G:
#     memo = {}
#
# def no_adj_sum(array, cur, i):
#     anchor = f'{cur},{i}'
#     if anchor in G.memo:
#         return G.memo[anchor]
#     if i >= len(array):
#         return cur
#     cur = cur + array[i]
#     G.memo[anchor] = max(no_adj_sum(array, cur, i + 2), no_adj_sum(array, cur, i + 3))
#     return G.memo[anchor]


def maxSubsetSumNoAdjacent(array):
    result = [(0, array[0]), (1, array[1])]
    while True:
        new_result = []
        for elem in result:
            if elem[0] + 2 >= len(array):
                continue
            new_result.append((elem[0]+2, elem[1] + array[elem[0]+2]))
            if elem[0] + 3 >= len(array):
                continue
            new_result.append((elem[0]+3, elem[1] + array[elem[0]+3]))

        result = new_result
        if result[-1][0] >= len(array) - 1:
            break

    return sorted(result, key=lambda x: x[1])[-1][1]

print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))
