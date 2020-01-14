
'''
테스트 1 〉	통과 (1603.67ms, 10.8MB)
테스트 2 〉	통과 (1504.04ms, 10.8MB)
테스트 3 〉	통과 (1.31ms, 10.9MB)
테스트 4 〉	통과 (4.86ms, 10.8MB)
테스트 5 〉	통과 (42.29ms, 10.8MB)
테스트 6 〉	통과 (2.61ms, 10.8MB)
테스트 7 〉	통과 (1.35ms, 10.8MB)
테스트 8 〉	통과 (10.41ms, 10.8MB)
'''

class G:
    target = 0
    ways = 0

graph = {

}

def dfs(here, visited=[], sum=0):
    visited.append(here)
    sum += graph[here]['value']
    if not graph[here]['adj']:
        if sum == G.target:
            G.ways += 1
    for node in graph[here]['adj']:
        if node not in visited:
            dfs(node, visited[:], sum)


def solution(numbers, target):

    graph['start'] = {'value': 0, 'adj': ['0A', '0B']}
    G.target = target

    for i in range(len(numbers) - 1):
        graph[f'{i}A'] = {'value': numbers[i], 'adj': [f'{i+1}A', f'{i+1}B']}
        graph[f'{i}B'] = {'value': 0-numbers[i], 'adj': [f'{i+1}A', f'{i+1}B']}

    i += 1
    graph[f'{i}A'] = {'value': numbers[i], 'adj': []}
    graph[f'{i}B'] = {'value': 0 - numbers[i], 'adj': []}

    dfs('start')

    return G.ways


# print(solution([1, 1, 1, 1, 1], 3))
print(solution([0, 1, 3], 2))

# 깔끔한 풀이
# solution 은 numbers 와 target 이 주어졌을 때 target 을 만들 수 있는 모든 경우의 수를 리턴하는 재귀함수
# 스탭을 밟아나갈때 마다 numbers 안의 '현재 스탭의 수' (numbers 의 0 번째 요소)를 제거하며,
# target - '현재 스탭의 수' 와 target + '현재 스탭의 수' 를 재귀호출 한다.
# 그래프를 안 쓰고 풀었다는 점도 훌륭.
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

'''
테스트 1 〉	통과 (385.54ms, 10.7MB)
테스트 2 〉	통과 (383.29ms, 10.8MB)
테스트 3 〉	통과 (0.41ms, 10.8MB)
테스트 4 〉	통과 (1.47ms, 10.8MB)
테스트 5 〉	통과 (12.05ms, 10.7MB)
테스트 6 〉	통과 (0.80ms, 10.7MB)
테스트 7 〉	통과 (0.42ms, 10.6MB)
테스트 8 〉	통과 (3.11ms, 10.7MB)
'''
