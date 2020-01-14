from collections import defaultdict, Counter
from functools import reduce
from itertools import combinations

cache = defaultdict(lambda: [])

def match(s1, s2):
    '''
    s1 과 s2 의 길이가 같음을 상정합니다.
    :param s1: 에스터리스크를 포함한 패턴
    :param s2: 문자열
    :return: 매치 여부
    '''
    for i in range(len(s1)):
        if s1[i] == '*':
            continue
        if s1[i] != s2[i]:
            return False
    return True


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(lambda a, b: a*b, range(n, n-r, -1), 1)
    denom = reduce(lambda a, b: a*b, range(1, r+1), 1)
    return numer // denom


def solution(user_id, banned_id):
    answer = 1
    ban_counter = Counter(banned_id)
    match_counter = {x: 0 for x in banned_id}

    for id_ in user_id:
        cache[len(id_)].append(id_)

    for id_ in banned_id:
        temp = 0
        for elem in cache[len(id_)]:
            if match(id_, elem):
               temp += 1
        match_counter[id_] = temp

    for key in ban_counter:
        answer *= ncr(match_counter[key], ban_counter[key])

    return answer


user_ids = ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
banned_ids = ['fr*d*', 'abc1*3']

# print(solution(user_ids, banned_ids)) # 2 가 답

# print(solution(user_ids, ['*rodo', '*rodo', '******'])) # 2가 답

print(solution(user_ids, ['fr*d*', '*rodo', '******', '******'])) # 3 이 답



