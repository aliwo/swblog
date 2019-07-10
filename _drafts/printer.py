from collections import deque

class G:
    shot = 0

def is_priority(priorities):
    '''
    0 번째 요소가 가장 우선 순위가 높은지 체크합니다.
    '''
    first_elem = priorities[0]
    for i in range(1, len(priorities)):
        if first_elem < priorities[i]:
            return False

    return True

def solution(priorities, location):
    '''
    리스트의 0번째 요소를 삭제하거나 0번째 요소에 추가하는 건 시간이 어마어마하게 든다.
    그렇다고 heapfy 를 하면 리스트의 순서가 뒤죽 박죽이 되어 버린다.
    어떻게 하노...
    -> 아니 그냥 큐나 덱을 쓰면 되는 것이었다.

    최악의 경우는 가장 우선 순위가 높은 요소가 맨 뒤에 있는 경우.
    '''
    priorities = deque(priorities)

    while priorities:
        if is_priority(priorities): # 가장 우선순위가 높은 요소를 뽑았을 경우
            priorities.popleft()
            G.shot += 1
            if location == 0:
                return G.shot
            location -= 1
        else:
            priorities.append(priorities.popleft())
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1


