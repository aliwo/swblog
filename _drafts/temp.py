def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    # 종류별 옷의 수
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer

