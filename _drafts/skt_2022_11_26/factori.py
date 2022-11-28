def fives():
    num = 5
    while True:
        yield num
        num *= 5


def solution(n) -> int:
    result = 0
    gen = fives()
    divider = next(gen)
    while divider <= n:  # 최신 python 이면 divider := next(gen) 가능!
        result += n // divider
        divider = next(gen)
    return result


# print(solution(3))  # 0
# print(solution(5))  # 1
# print(solution(10))  # 2
# print(solution(14))  # 2
# print(solution(15))  # 3
# print(solution(25))  # 6개
# print(solution(125))  # 31개. 5로 나누면 25, 25로 나누면 5, 그리고 125로 나누면1. 따라서 25 + 5 + 1 = 31

# gen = fives()
# print(next(gen))
# print(next(gen))
# print(next(gen))



####################### 백준
# n = int(input())

# 와 이게 훨 간결하다.
def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt

print(five_count(5))
print(five_count(125))
