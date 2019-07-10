# 아니 정렬 안 쓸 때 보다 더 느린데... 시간 체크 5개가 다 나가리임. (전에는 3개라도 통과했는데)


class G:
    boats = [[0, 0]]
    undone = 0


def insert(p, start, limit):
    if p == 0:
        return
    if G.undone == len(G.boats):
        G.boats.append([p, 0])
        return

    # 가장 딱 맞아들어가는 자리를 찾는다.
    max_value = [len(G.boats), 0, p]
    for i in range(start, len(G.boats)):
        right = G.boats[i][0] + p
        left = G.boats[i][1] + p
        max_candidate = max(right, max_value[2], left)

        if right <= limit and max_candidate == right:
            max_value = [i, 1, p]
        elif left <= limit and max_candidate == left:
            max_value = [i, 0, p]

    # 들어갈 자리가 없었다면
    if max_value[0] == len(G.boats):
        G.boats.append([p, 0])
        return

    # 들어갈 자리가 있었다면
    old = G.boats[max_value[0]][max_value[1]]
    G.boats[max_value[0]][max_value[1]] = max_value[2]
    insert(old, max_value[0]+1, limit)



def solution(people, limit):
    for p in people:
        if p == limit: # 너무 무거운 사람
            G.boats.insert(G.undone, [p, 0])
            G.undone += 1
            continue
        insert(p, G.undone, limit)
    return len(G.boats)


# solution([1, 2, 4, 6, 8, 9, 6, 4, 10], 10)
solution([70, 50, 80, 50], 100)
print(len(G.boats))
