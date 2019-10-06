
seen = []
orders = []
graph = {
    '1': {'win': {'2'}, 'lose': set()},
    '2': {'win': {'5'}, 'lose': {'1', '3', '4'}},
    '3': {'win': {'2'}, 'lose': {'4'}},
    '4': {'win': {'2', '3'}, 'lose': set()},
    '5': {'win': set(), 'lose': {'2'}},
}

def topological_orders():
    for key, value in graph.items():
        if len(value.get('lose')) == 0 and key not in seen:
            for loser in value.get('win'):
                graph[loser]['lose'].discard(key)
            seen.append(key)

            topological_orders()

            for loser in value.get('win'):
                graph[loser]['lose'].add(key)
            seen.pop()

    if len(seen) == len(graph):
        orders.append(seen[:])


topological_orders()
print(orders)

