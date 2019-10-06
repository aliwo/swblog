# 위상순서를 전부 뽑아내는 것 만으로도 시간초과다.
# 2019-10-04 오후 2시. 반타작에 성공. 나머지는 시간 초과.

# 리스트 복사 안쓰는데도 key value 를 2번 순회하니까 더 느려졌는데?

seen = []
graph = {}
obscure = set()

def topological_orders():

    temp_obscure = []

    for key, value in graph.items():
        if len(value.get('lose')) == 0 and key not in seen:
            temp_obscure.append(key)

    if len(temp_obscure) >= 2:
        [obscure.add(key) for key in temp_obscure]

    for key, value in graph.items():
        if len(value.get('lose')) == 0 and key not in seen:

            for loser in value.get('win'):
                graph[loser]['lose'].discard(key)
            seen.append(key)

            topological_orders()

            for loser in value.get('win'):
                graph[loser]['lose'].add(key)
            seen.pop()


def solution(n, results):
    global graph
    graph = {i: {'win': set(), 'lose': set()} for i in range(1, n+1)}
    for result in results:
        graph[result[0]]['win'].add(result[1])
        graph[result[1]]['lose'].add(result[0])

    topological_orders()

    return n - len(obscure)


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
