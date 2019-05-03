

def solution(N):
    max_gap = 0
    start = 0
    for i, char in enumerate(bin(N)):
        if char == '1':
            if start == 0:
                start = i
            else:
                cur_gap = i - start - 1
                if max_gap < cur_gap:
                    max_gap = cur_gap
                start = i
    return max_gap


# https://stackoverflow.com/questions/48951591/python-find-longest-binary-gap-in-binary-representation-of-an-integer-number
# codility 문제랑은 결과가 좀 다르다. (100 이면 gap 을 2라고 판단한다.)
# codility 에서 돌려보았을떄 위 함수랑 걸리는 시간은 0.036 초로 똑같다. 무엇을 돌려도 이 값이 나오는데, default 값인 건지
# 아니면 둘 다 너무 빨라서 최소 수치가 나오는건지 모르겠다.
def max_gap(x):
    max_gap_length = 0
    current_gap_length = 0
    for i in range(x.bit_length()):
        if x & (1 << i):
            # Set, any gap is over.
            if current_gap_length > max_gap_length:
                max_gap_length = current_gap_length
            current_gap_length = 0
        else:
            # Not set, the gap widens.
            current_gap_length += 1
    # Gap might end at the end.
    if current_gap_length > max_gap_length:
        max_gap_length = current_gap_length
    return max_gap_length


print(solution(2147483647))

# 예제 목록
#
#
# ▶
# extremes
# n=1, n=5=101_2 and n=2147483647=2**31-1
# ✔
# OK
# ▶
# trailing_zeroes
# n=6=110_2 and n=328=101001000_2
# ✔
# OK
# ▶
# power_of_2
# n=5=101_2, n=16=2**4 and n=1024=2**10
# ✔
# OK
# ▶
# simple1
# n=9=1001_2 and n=11=1011_2
# ✔
# OK
# ▶
# simple2
# n=19=10011 and n=42=101010_2
# ✔
# OK
# ▶
# simple3
# n=1162=10010001010_2 and n=5=101_2
# ✔
# OK
# ▶
# medium1
# n=51712=110010100000000_2 and n=20=10100_2
# ✔
# OK
# ▶
# medium2
# n=561892=10001001001011100100_2 and n=9=1001_2
# ✔
# OK
# ▶
# medium3
# n=66561=10000010000000001_2
# ✔
# OK
# ▶
# large1
# n=6291457=11000000000000000000001_2
# ✔
# OK
# ▶
# large2
# n=74901729=100011101101110100011100001
# ✔
# OK
# ▶
# large3
# n=805306373=110000000000000000000000000101_2
# ✔
# OK
# ▶
# large4
# n=1376796946=1010010000100000100000100010010_2
# ✔
# OK
# ▶
# large5
# n=1073741825=1000000000000000000000000000001_2
# ✔
# OK
# ▶
# large6
# n=1610612737=1100000000000000000000000000001_2
# ✔
# OK
#
#
