from collections import defaultdict
from functools import reduce

graph = defaultdict(lambda: [])


def num_of_diff_words(word_a, word_b):
    '''
    word_a 와 word_b 의 길이가 같다는 것을 전제합니다!
    '''
    diff = 0
    for a, b in zip(word_a, word_b):
        if a != b:
            diff += 1
    return diff


def add_node(node):
    added_nodes = []
    for key, value in graph.items():
        if num_of_diff_words(node, key) == 1:
            added_nodes.append(key)
            value.append(node)
    graph[node] = added_nodes


def find_all_paths(start, end, path=[]):
    '''
    start 로 부터 시작해서 end 에 도달하는
    모든 경로를 리턴합니다.
    '''
    path = path + [start]
    if start == end:
        return [path]
    if graph[start] == []:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def solution(begin, target, words):

    # 그래프를 형성합니다.
    # 서로 한 단어씩만 차이 나는 단어끼리 연결됩니다.
    for word in words:
        add_node(word)
    add_node(begin)

    if target not in words:
        return 0

    return len(reduce(lambda x, y: x if len(x) < len(y) else y, find_all_paths(begin, target))) - 1 # 시작지점은 안 센다.

'''
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.33ms, 10.7MB)
테스트 3 〉	통과 (1.02ms, 10.8MB)
테스트 4 〉	통과 (0.06ms, 10.7MB)
테스트 5 〉	통과 (0.04ms, 10.8MB)
'''

# assert solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]) == 4


def solution(begin, target, words):
    answer = 0
    Q = [begin] # queue 처럼 쓰겠다는 건가>

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target: # 기저 사례: 시작단어 == 끝단어 일때
                return answer
            for i in range(len(words) - 1, -1, -1): # words 를 역순회전 합니다.
                word_2 = words[i]
                if sum([x != y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words._pop(i))

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1

assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
# assert solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
'''
테스트 1 〉	통과 (0.06ms, 10.8MB)
테스트 2 〉	통과 (0.11ms, 10.6MB)
테스트 3 〉	통과 (0.46ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.8MB)
테스트 5 〉	통과 (0.04ms, 10.7MB)
'''


# 테스트 3에서 그래프는 1.02ms, 리스트는 0.46ms

