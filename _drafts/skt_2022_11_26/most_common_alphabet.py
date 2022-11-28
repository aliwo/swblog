from itertools import takewhile
from collections import Counter


def solution(s) -> str:
    s = s.lower()
    counted = Counter(s)
    commons = counted.most_common()
    top_most_common = commons[0][1]
    return "".join(
        sorted(
            elem[0] for elem in list(takewhile(lambda x: x[1] == top_most_common, commons))
        )
    )


# print(solution("aAb"))
# print(solution("BA"))
# print(solution("Bba"))
# print(solution("aAabBb"))  # ab
print(solution("Z"))  # z
print(solution("abcAbCABC"))  # z
