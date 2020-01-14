
def fill(a):
    if len(a) == 1:
        return a[0], a[0], a[0], a[0]
    if len(a) == 2:
        return a[0], a[1], a[0], a[1]
    if len(a) == 3:
        return a[0], a[1], a[2], a[0]
    if len(a) == 4:
        return a[0], a[1], a[2], a[3]


def solution(numbers):
    return ''.join(sorted([str(x) for x in numbers], key=fill, reverse=True))

print(solution([1, 0,0,0,0,0,0,0,0,0,0,0]))
print(solution([0,0,0,0,0,0,0,0,0,0,0]))
print(solution([3, 2,0,0,0,0,0,0,0,0,0,0]))
