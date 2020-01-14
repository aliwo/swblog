# https://programmers.co.kr/learn/courses/30/lessons/43164
# tickets 를 모두 소진하는 경우의 수 중
# 알파벳 순서가 가장 앞서는 경우의 수를 리턴해야 한다.

from collections import defaultdict

class G:
    visited_list = []
    tickets_num = 0

graph = defaultdict(lambda: [])

def dfs(before, here, i, visited=[]):
    '''
    visited 에 간선을 저장하는 dfs 를 쓰면 됨!
    '''
    visited.append(f'{before},{here},{i}')

    if len(visited) == G.tickets_num + 1:
        G.visited_list.append([x.split(',')[1] for x in visited])

    for i in range(len(graph[here])):
        if f'{here},{graph[here][i]},{i}' not in visited:
            dfs(here, graph[here][i], i, visited[:]) # 한 번 탐색이 끝나도 계속 다른 경우의 수를 찾으려면 복사가 필요함.


def solution(tickets):
    G.tickets_num = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    dfs('START', 'ICN', 0)

    if not G.visited_list:
        return []

    return sorted(G.visited_list)[0]

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
