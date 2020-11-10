

class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y


def calc(from_, to, n):
    if from_ == to:
        return 0
    big, small = (from_, to) if from_ > to else (to, from_)
    return min(big - small, (n - big) + (0 + small))


def calc_node(from_node, to_node, n):
    '''
    x 축 이동 + y 축 이동 + 엔터 한 번
    ... 사실 n*n 만큼 나중에 더해도 됨...
    '''
    if from_node.x == 0 and from_node.y == 4:
        print('?')
    print(f'{from_node.x} {from_node.y}  에서 {to_node.x} {to_node.y} 으로 이동 { calc(from_node.x, to_node.x, n) + calc(from_node.y, to_node.y, n)}!')
    return calc(from_node.x, to_node.x, n) + calc(from_node.y, to_node.y, n) + 1


def solution(n, board):
    numbers = sorted([Node(board[i][j], i, j)
                      for i in range(len(board))
                      for j in range(len(board[i]))], key=lambda x: x.value)

    return (calc_node(Node(0,0,0), numbers[0], n)) \
           + sum(calc_node(numbers[i], numbers[i+1], n) for i in range(len(numbers) - 1))


# print(solution(3, [[3, 5, 6], [9, 2, 7], [4, 1, 8]]	))
# print(solution(2, [[2, 3], [4, 1]]))
# print(solution(4, [[11, 9, 8, 12], [2, 15, 4, 14], [1, 10, 16, 3], [13, 7, 5, 6]]))
print(solution(5, [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]))