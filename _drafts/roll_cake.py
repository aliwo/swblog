from collections import Counter

def solution(topping):
    answer = 0

    left = set()
    right = Counter(topping)

    for i, elem in enumerate(topping):
        left.add(elem)
        right[elem] -= 1
        if right[elem] == 0:
            del right[elem]

        if len(left) == len(right):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
# print(solution([1, 2, 3, 1, 4]))