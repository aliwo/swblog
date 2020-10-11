
# DP 문제. 풀어본 적 있다... 어떻게 풀었었지?
# 현재가 3이라면, 1만큼 점프했을 때, 2만큼 점프했을 때, 3만큼 점프했을 때 이렇게 3개로 나눠서 퍼져 나갔던거 같은데
# 만약 무조건 index 에 적힌 수 만큼만 점프해야 되면 DP 문제가 되고, 이 문제는 1~index 사이에서 골라서
# 점프할 수가 있으니까 탐욕법으로 풀 수 있다!

def minNumberOfJumps(array):
    min_jump = float('inf')
    jumps = [(0, 0)] # (사용한 점프 수, 현재 인덱스)
    while jumps:
        new_jump = []
        for jump in jumps:
            for i in range(1, array[jump[1]] + 1):
                if jump[1] + i >= len(array) - 1: # 끝에 도달한 경우
                    min_jump = min(jump[0] + 1, min_jump)
                else:
                    new_jump.append((jump[0] + 1, jump[1] + i))
        jumps = new_jump
    return min_jump


print(minNumberOfJumps([3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]))