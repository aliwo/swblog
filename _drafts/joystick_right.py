# 양쪽  False 의 거리가 같을 경우 '오른쪽' 으로 이동하는 알고리즘
# 2019-09-13 에 정답으로 인정되는 것 확인

def alter_alpha(to):
    num = ord(to)
    return num - 65 if num < 79 else 90 - num + 1


def alter_cursor(done, i):
    '''
    만약 left 와 right 가 같은 경우일 지라도,
    남아 있는 False 에 따라서 최적해가 다르다.
    '''
    left = right = i
    cnt = 1

    for _ in range(len(done) // 2):
        left = left - 1 if left > 0 else len(done) - 1
        right = right + 1 if right < len(done) - 1 else 0
        if done[right] == False:
            return right, cnt
        if done[left] == False:
            return left, cnt
        cnt += 1

    return [-1, 0] # name 이 완성되었음.

def solution(name):
    '''
    done 을 쓰지 않고 해결할 방법은 없을까?
    '''
    cnt = 0
    done = [False] * len(name)

    for i in range(len(name)):
        if name[i] == 'A':
            done[i] = True

    i = 0
    while i != -1:
        cnt += alter_alpha(name[i])
        done[i] = True
        i, alter_cnt = alter_cursor(done, i)
        cnt += alter_cnt
    return cnt

print(solution('AABAAAAAAAAAAAAB'))
