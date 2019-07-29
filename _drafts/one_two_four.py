

def solution(n):
    '''
    n 은 5억 까지 올라간다. 1부터 순회하는 방식으로는 절대 시간 안에 못 맞춘다.
    1 2 4 나라가 아니라 a b c 나라라고 해도 무리는 없다.
    설마 이걸 dp 로 푼다고?
    :param n:
    '''
    remainders = []

    div, remainder = divmod(n, 3)
    remainders.append(remainder)
    while div > 1:
        div, remainder = divmod(div, 3)
        remainders.append(remainder)

    remainders.append(div)

    for i in range(len(remainders)):
        if remainders[i] == 0:
            remainders[i] = 1
        elif remainders[i] == 1:
            remainders[i] = 2
        elif remainders[i] == 2:
            remainders[i] = 4

    return remainders

print(solution(1))
