# 바람직한 동적 계획법
def solution(N, number):
    S = [{N}]
    # S[i] 는 i 개의 N 으로 만들 수 있는 모든 수의 조합을 얘기한다.
    # 예를 들어 S[1} 이면 N 이 1개 있으므로, N 하나 밖에 못 만든다.

    for i in range(2, 9): # N 이 2개 있을 때 부터 N이 8개 있을 때 까지.
        lst = [int(str(N)*i)] # '나열' 해서 만들어진 수가 lst[0]
        for X_i in range(0, int(i / 2)): # 왜 i 의 절반까지만 회전하지?
            for x in S[X_i]: # S 가 이중 배열이므로 X 는 S[X_i] 에 있는 모든 요소가 된다.
                for y in S[i - X_i - 2]: # y는 i - X_i - 2... 무엇?
                    lst.append(x + y) # 결국 x와 y를 계산하는 건데
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1

'''
테스트 1 〉	통과 (4.98ms, 12MB)
테스트 2 〉	통과 (0.06ms, 10.8MB)
테스트 3 〉	통과 (2.22ms, 10.8MB)
테스트 4 〉	통과 (745.14ms, 160MB)
테스트 5 〉	통과 (734.10ms, 139MB)
테스트 6 〉	통과 (0.47ms, 11MB)
테스트 7 〉	통과 (0.46ms, 10.9MB)

S.append() 할 때 중복을 제거한 set 이 아닌, 리스트를 그대로 저장하기 때문에 테스트 4 와 테스트 5에서 극악의 속도저하를
보여준다.
'''

# 승원이가 DP 조금 수정한 버전
def solution(N, number):
    cache = [set(), {N}] # 계산의 단순화를 위해 0번은 비워둔다.

    for i in range(2, 9): # N 이 2개 있을 때 부터 N이 8개 있을 때 까지.
        lst = [int(str(N)*i)] # '나열' 해서 만들어진 수가 lst[0]
        for X_i in range(0, int(i / 2)+1): 
            for x in cache[X_i]:
                for y in cache[i - X_i]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        s_lst = set(lst)
        if number in s_lst:
            return i
        cache.append(s_lst)
    return -1
'''
테스트 1 〉	통과 (3.91ms, 10.9MB)
테스트 2 〉	통과 (0.07ms, 10.8MB)
테스트 3 〉	통과 (0.07ms, 10.8MB)
테스트 4 〉	통과 (14.11ms, 14.3MB)
테스트 5 〉	통과 (11.90ms, 13.6MB)
테스트 6 〉	통과 (0.19ms, 10.8MB)
테스트 7 〉	통과 (0.19ms, 10.8MB)
'''

# 무려 dfs 로 푸는 솔루션
number = None
N = None
answer = 987654321
def dfs(count, value):
    global N, number, answer
    if value == number:
        answer = min(answer, count)
    if count == 8:
        return
    for a in range(0,8-count):
        soo = int(f"{N}" * (a+1))
        dfs(count + a+1, value + soo)
        dfs(count + a+1, value - soo)
        dfs(count + a+1, value * soo)
        if value % N == 0: dfs(count + a+1, value / soo)

def solution(_, __):
    global N, number, answer
    N, number = _, __
    dfs(0,0)
    if answer == 987654321: return -1
    return answer
'''
테스트 1 〉	통과 (91.15ms, 10.8MB)
테스트 2 〉	통과 (110.40ms, 10.9MB)
테스트 3 〉	통과 (94.75ms, 10.8MB)
테스트 4 〉	통과 (96.25ms, 10.8MB)
테스트 5 〉	통과 (92.20ms, 10.7MB)
테스트 6 〉	통과 (91.35ms, 10.9MB)
테스트 7 〉	통과 (91.96ms, 10.9MB)

역시 DP 에는 속도로 상대가 안된다.
'''


# Brute Force 로 풀었다는 솔루션



