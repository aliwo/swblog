strategy = '''
2번째로 높은 기둥 부터 
레이저를 가로 방향으로 쏘면서 내려가는 방식으로 접근한다.
'''


def waterArea(heights):
    if len(heights) <= 1:
        return 0

    result = 0
    # 2 번째로 높은 기둥을 발견합니다.
    mx = max(heights[0], heights[1])
    secondmax = min(heights[0], heights[1])
    for i in range(2, len(heights)):
        if heights[i] > mx:
            secondmax = mx
            mx = heights[i]
        elif heights[i] > secondmax:
            secondmax = heights[i]

    # 2 번째로 높은 기둥 부터 레이저를 쏩니다.
    for i in reversed(range(1, secondmax+1)):
        start = -1
        for j, elem in enumerate(heights):
            if elem == 0:
                continue
            if elem - i >= 0: # 기둥을 발견했을 때
                if start != 0-1:
                    result += j - start - 1
                start = j

    return result


# print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))
# print(waterArea([1]))
print(waterArea([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]))