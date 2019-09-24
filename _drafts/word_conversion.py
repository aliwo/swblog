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


assert solution('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]) == 4
