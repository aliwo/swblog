def solution(N, number):
    S = [{N}] # S 의 0번째 요소만 set 이고 나머지는 list 이다.
    for i in range(2, 9):
        lst = [int(str(N)*i)] # '나열' 해서 만들어진 수가 lst[0]
        for X_i in range(0, int(i / 2)): # 왜 i 의 절반까지만 회전하지?
            for x in S[X_i]: # S 가 이중 배열이므로 X 는 S[X_i] 에 있는 모든 요소가 된다.
                for y in S[i - X_i - 2]: # y는 i - X_i - 2... 무엇?
                    print('i:{}  x:{}  y:{}  S:{}'.format(i, x, y, S))
                    lst.append(x + y) # 결국 x와 y를 계산하는 건데
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1

solution(5, 5555)
