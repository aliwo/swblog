from collections import OrderedDict

def validate_skill_tree(skill, elem):

    # ordered dict 이어야 합니다.
    store = OrderedDict()

    for char in skill:
        store[char] = len(elem)

    for i in range(len(elem)):
        if elem[i] in skill:
            store[elem[i]] = i

    prev_value = 0
    for key, value in store.items():
        if value < prev_value:
            return False
        prev_value = value

    return True


def solution(skill, skill_trees):
    possible = 0

    for elem in skill_trees:
        if validate_skill_tree(skill, elem):
            possible += 1

    return possible
