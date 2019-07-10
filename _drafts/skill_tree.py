
def validate_k(k, pre_skill):
    for elem in pre_skill:
        if elem == k:
            return False
    return True


def validate_skill_tree(skill, skill_tree):
    last_j = len(skill_tree)
    for i in range(len(skill)-1, -1, -1):
        for j in range(len(skill_tree)):
            if skill_tree[j] == skill[i]:
                for k in range(j, last_j):
                    if not validate_k(skill_tree[k], skill[0:i]):
                        return False
            last_j = j # skill_tree 에서 마지막 j 의 위치

    return True

def solution(skill, skill_trees):
    possible = 0

    for elem in skill_trees:
        if validate_skill_tree(skill, elem):
            possible += 1

    return possible

