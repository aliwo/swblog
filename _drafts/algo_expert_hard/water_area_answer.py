
def waterArea(heights):
    '''
    와 개쩐다... 난 수위가 높으면
    그 만큼 시간이 오래 걸리는 데
    얘는 딱 2번 회전해서 끝내네

    특정 위치의 수위를 maxes 에 기록한다는 것이 참신하다.
    '''
    maxes = [0 for x in heights]

    # left max 를 구해서 maxes 에 저장
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)

    # <- 방향으로 회전. right max 를 구하는 동시에
    # maxes 값을 조절한다. 해당 위치에서 최대로 가질 수 있는 수위 - 해저의
    # 기둥이 잡아먹는 값.
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i]) # minHeight 이 곧 water level
        if height < minHeight:
            maxes[i] = minHeight - height # height 은 해저의 기둥값.
        else:
            maxes[i] = 0 # 기둥이 수위보다 높으면 물은 0
        rightMax = max(rightMax, height)

    return sum(maxes)