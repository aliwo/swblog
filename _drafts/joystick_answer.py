
def solution(name):
    count = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {}
    indexes = []
    current_idx = 0
    n = len(name)
    for i in range(len(alpha)):
        d[alpha[i]] = min(i, 26 - i)
    # print(d)
    for i in range(n):
        num = d[name[i]]
        count += num
        if num != 0:
            indexes.append(i)
    # indexes 는 A가 아닌 문자열들의 위치가 오름차순으로 들어있다.
    # current_idx 는 0부터 시작. 현재 커서가 어디있는지를 가리킴
    # min(abs(it - current_idx), n - abs(it - current_idx)) 현재 커서로 부터 오른쪽으로 가는 거리 혹은
    # 왼쪽으로 가는 거리 중 더 짧은 값
    while True:
        if len(indexes) == 0:
            break
        min_dist = 99 # 매우 큰 값으로 초기화,
        min_idx = 0
        for it in indexes: # 현재 존재하는 False 후보 중, 가장 가까운 거리를 찾는다.
            min_dist2 = min(abs(it - current_idx), n - abs(it - current_idx))
            if min_dist2 < min_dist:
                min_dist = min_dist2
                min_idx = it
        count += min_dist
        indexes.remove(min_idx)
        current_idx = min_idx

    return count

print(solution('AABAAAAAAAAAAB')) # 오른쪽 끝에서 왼쪽 끝으로 넘어갈 수 있다하면 답은 6

