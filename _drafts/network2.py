
# 심플함은 만점이지만... 정말 말도 안되는 방법이네 ㅋㅋㅌㅋㅋㅋ

def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j] # 같은 네트워크면 temp[k]로 통일하는거야 지금???????
    return len(set(temp))


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))


# temp 의 변화 -> 0 1 2
# 1 1 2
# 1 1 2
# 1 1 2
# 1 1 2
