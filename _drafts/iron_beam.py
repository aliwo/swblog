def solution(arrangement):
    pieces = 0
    cache = [] # stack

    for i in range(len(arrangement)):
        if arrangement[i] == '(':
            cache.append(i)
            if arrangement[i+1] != ')':
                pieces += 1

        else:
            elem = cache.pop()
            if i - elem == 1: # 레이저
                pieces += len(cache)

    return pieces

solution('()(((()())(())()))(())')



