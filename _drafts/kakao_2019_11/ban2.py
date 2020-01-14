from collections import defaultdict


cache = defaultdict(lambda: [])


def match(s1, s2):
    '''
    :param s1: 에스터리스크를 포함한 패턴
    :param s2: 문자열
    :return: 매치 여부
    '''
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] == '*':
            continue
        if s1[i] != s2[i]:
            return False
    return True


def pick(acc, banned_id, comb=[]):
    '''
    하나를 고르고, 다시 재귀호출
    '''

    if not banned_id:
        acc.add(frozenset(comb))

        return acc

    temp = banned_id.pop() # 패턴을 하나 뽑습니다.

    for i, elem in enumerate(cache[len(temp)]):
        if match(temp, elem):
            cache[len(temp)][i] = ''
            comb.append(elem)
            acc = pick(acc, banned_id)
            cache[len(temp)][i] = elem
            comb.pop()

    banned_id.append(temp)
    return acc


def solution(user_id, banned_id):
    for id_ in user_id:
        cache[len(id_)].append(id_)

    return len(pick(set(), banned_id))


user_ids = ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
banned_ids = ['fr*d*', 'abc1*3']

# print(solution(user_ids, banned_ids)) # 2 가 답
# print(solution(user_ids, ['*rodo', '*rodo', '******'])) # 2가 답
print(solution(user_ids, ['fr*d*', '*rodo', '******', '******'])) # 3 이 답



