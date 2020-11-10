from itertools import chain
from collections import defaultdict


def solution(logs):
    temp = defaultdict(lambda: dict())
    suspects = defaultdict(lambda: [])
    for log in logs:
        student_id, p_id, p_score = log.split()
        temp[student_id][p_id] = p_score

    for key, value in temp.items():
        if len(value) >= 5:
            suspects[frozenset(value.items())].append(key)

    suspects = sorted(chain(*[value for value in suspects.values() if len(value) >= 2]))
    return suspects if suspects else ['None']


# print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0001 7 80", "0001 8 80", "0001 10 90",
#                 "0002 3 95", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100",
#                 "0003 99 90","0003 98 90","0003 97 90","0003 96 90","0003 95 90",
#                 "0004 99 90","0004 98 90","0004 97 90","0004 95 90","0004 96 90", ]))
# print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0001 7 80", "0001 8 80", "0001 10 90",
#                 "0003 99 90","0003 98 90","0003 97 90","0003 96 90","0003 95 90",
#                 "0004 99 90","0004 98 90","0004 97 90","0004 95 90","0004 96 90",
#                 "0002 3 95", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100",]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "2001 1 100", "2001 2 100", "2001 4 100", "2001 7 95", "2001 9 100", "2002 1 95", "2002 2 100", "2002 4 100", "2002 7 100", "2002 9 100"]))
# print(solution(["1901 10 50", "1909 10 50"]))
