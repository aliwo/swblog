
# 내가 저번에 한 번 비효율적인 방법대로 푸니까... 계속 풀었던 방법대로 푸네...
# 처음부터 답지를 익히는 것도 효율적인 공부 방법인 것 같다.

# 심지어 이건 DP 가 아닌가???

def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0] # 현재 지점이 0이고, 현재 지점에서 최대한으로 쓸 수 있는 step 이 곧 steps
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i]) # 다음 스텝을 밟고 닿을 수 있는 최대 지점을 찾는다.
        steps -= 1
        if steps == 0:
            jumps += 1 # 다음 지점으로 이동, jump 횟수를 추가
            steps = maxReach - i # steps 를 충전

    return jumps + 1

print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))