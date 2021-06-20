# 위상순서를 전부 뽑아내는 것 만으로도 시간초과다.
# 2019-10-04 오후 2시. 반타작에 성공. 나머지는 시간 초과.

seen = []
orders = []
graph = {}

def topological_orders():
    for key, value in graph.items():
        if len(value.get('lose')) == 0 and key not in seen:
            for loser in value.get('win'):
                graph[loser]['lose'].discard(key)
            seen.append(key)

            topological_orders()

            for loser in value.get('win'):
                graph[loser]['lose']._add(key)
            seen.pop()

    if len(seen) == len(graph):
        orders.append(seen[:])


def solution(n, results):
    answer = 0
    global graph
    graph = {i: {'win': set(), 'lose': set()} for i in range(1, n+1)}
    for result in results:
        graph[result[0]]['win']._add(result[1])
        graph[result[1]]['lose']._add(result[0])

    topological_orders()

    for j in range(n):
        rank = [orders[i][j] for i in range(len(orders))]
        for elem in rank:
            if elem != rank[0]:
                break
        else:
            answer +=1

    return answer

