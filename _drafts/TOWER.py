# https://programmers.co.kr/learn/courses/30/lessons/42588?language=python3

class G:
    result = []
    stack = []


def solution(heights):
    '''
    답을 저장하기 위한 0으로 채워진 리스트를 만들어야 함.
    '''
    # heights = [6,9,5,7,4]
    # heights = [3,9,9,3,5,7,2]
    # heights = [1,5,3,6,7,6,5]
    G.result = [0 for _ in range(len(heights))]

    while heights:
        G.stack.append((len(heights), heights._pop()))
        if heights and heights[-1] > G.stack[-1][1]:
            while heights and  G.stack and heights[-1] > G.stack[-1][1]:
                G.result[G.stack.pop()[0]-1] = len(heights)

    return G.result

print(solution([1,5,3,6,7,6,5]))
