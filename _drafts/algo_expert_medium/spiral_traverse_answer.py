
notice = '''
답지는 "밟은 지점을 기록하지 않아도 되는 방법" 을 사용해서 간단하게 접근했다. (또한, 현재의 진행방향을 기록할 필요도 없다)
그 비결은 "외곽만 순회하는 것" 전체 외곽을 한 번 순회 한 후
외곽 안 쪽의 사각형으로 범위를 좁힌다.
모든 사각형을 순회할 때 까지 반복한다.
'''

def spiralTraverse(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startRow <= endRow and startCol <= endCol:
        # 오른쪽으로 진행한다.
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # 아래쪽으로 진행한다.
        for row in range(startRow+1, endRow+1):
            result.append(array[row][endCol])

        # 왼쪽으로 진행한다.
        for col in reversed(range(startCol, endCol)):
            if startCol == endCol:
                break
            result.append(array[endRow][col])

        # 오른쪽으로 진행한다.
        for row in reversed(range(startRow, endRow)):
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        # 외곽(perimeter)을 좁혀 나간다.
        startRow += 1
        startCol += 1
        endCol -= 1
        endRow -= 1

    return result

