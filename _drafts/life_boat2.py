
class G:
    boats = [[0, 0]]
    undone = 0

def escalate(i, p, limit):
    if p == 0:
        return
    for j in range(i, len(G.boats)):
        if G.boats[j][0] == 0 and G.boats[j][1] + p <= limit:
            G.boats[j][0] = p
            return
        elif G.boats[j][1] == 0 and G.boats[j][0] + p <= limit:
            G.boats[j][1] = p
            return
    G.boats.append([p, 0])


def insert(p, limit):
    if p == 0:
        return
    if G.undone == len(G.boats):
        G.boats.append([p, 0])
        return

    for i in range(G.undone, len(G.boats)):
        right = G.boats[i][0] + p
        left = G.boats[i][1] + p

        if right <= limit:
            if left <= right or left > limit:
                old = G.boats[i][1]
                G.boats[i][1] = p
                if right == limit:
                    G.undone += 1
                escalate(i+1, old, limit)
                return
        if left <= limit:
            if right <= left or right > limit:
                old = G.boats[i][0]
                G.boats[i][0] = p
                if left == limit:
                    G.undone += 1
                escalate(i+1, old, limit)
                return


def solution(people, limit):
    for p in people:
        if p == limit: # 너무 무거운 사람
            G.boats.insert(G.undone, [p, 0])
            G.undone += 1
            continue
        insert(p, limit)
    return len(G.boats)


solution([70, 50, 80, 50], 100)
print(len(G.boats))
