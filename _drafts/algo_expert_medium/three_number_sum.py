from collections import defaultdict

# def threeNumberSum(array, targetSum):
#     '''
#     정렬하고 탐색을 시작하나
#     아니면 정렬 없이 답을 만들까.
#
#     two number sum 이면 딕셔너리 만들면 된다.
#     three number sum 이면 이중 루프 돌면서 딕셔너리를 look up 하면 되나?
#
#     '''
#     array.sort()
#     cache = {x: {y: True for y in array[i+1:]} for i, x in enumerate(array)}
#     result = []
#     for i in array:
#         for j in array[i:]:
#             if targetSum - (i + j) in cache[j]:
#                 result.append(sorted([i, j, targetSum - (i + j)]))
#
#     return result


def threeNumberSum(array, targetSum):
    '''
    정렬하고 탐색을 시작하나
    아니면 정렬 없이 답을 만들까.

    two number sum 이면 딕셔너리 만들면 된다.
    three number sum 이면 이중 루프 돌면서 딕셔너리를 look up 하면 되나?

    '''
    array.sort()
    cache = defaultdict(lambda: defaultdict(dict))
    result = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            for k in range(j+1, len(array)):
                cache[array[i]][array[j]][array[k]] = True

    for x, cache_2 in cache.items():
        for y, cache_3 in cache_2.items():
            if targetSum - (x + y) in cache_3:
                result.append(sorted([x, y, targetSum - (x + y)]))

    return result


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))
# print(threeNumberSum([1, 2, 3], 6))

