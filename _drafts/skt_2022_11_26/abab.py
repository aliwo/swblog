from itertools import takewhile
from typing import List, Dict


MEMO: Dict[str, bool] = dict()


def _process(word: str) -> bool:
    original_word = word
    while word != "a":
        if word in MEMO:  # DP
            return MEMO[word]

        # 앞의 a 그냥 제거 가능
        if word.startswith("a"):
            word = word[1:]
            continue
        # 뒤의 a 그냥 제거 가능
        if word.endswith("a"):
            word = word[:-1]
            continue
        # b 를 제거할 경우 1의 개수만큼
        if word.startswith("b") and word.startswith("b"):
            a_cnt = word.count("a")
            prefix_b_cnt = sum(1 for _ in takewhile(lambda c: c == "b", word))
            suffix_b_cnt = sum(1 for _ in takewhile(lambda c: c == "b", reversed(word)))
            if a_cnt == prefix_b_cnt == suffix_b_cnt:
                word = word[a_cnt:-a_cnt]
                continue

        MEMO[original_word] = False
        return False

    MEMO[original_word] = True
    return True


def solution(a: List[str]) -> List[bool]:
    return [_process(word) for word in a]


# print(
#     solution(
#         [
#             "abab",  # True
#             "bbab",  # False
#             "bababa",  # False
#             "bbbabababbbaa",  # True
#         ]
#     )
# )

# print(
#     solution(
#         [
#             "b"  # False
#         ]
#     )
# )

# print(
#     solution(
#         [
#             "bbbabababbbaa"  # True
#         ]
#     )
# )

# print(
#     solution(
#         [
#             "abbababababbba"  # False
#         ]
#     )
# )

# print(
#     solution(
#         [
#             "bab",  # True
#             "baba",  # True
#         ]
#     )
# )

print(
    solution(
        [
            "bab",  # True
            "bbaa",  # False
            "baba",  # True
        ]
    )
)


# processing = "bbabbb"
# min(
#     sum(1 for _ in takewhile(lambda c: c == "b", processing)),  # bb
#     sum(1 for _ in takewhile(lambda c: c == "b", reversed(processing))),  # bbb
# )