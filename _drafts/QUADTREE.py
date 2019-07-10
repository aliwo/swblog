# 예제는 모두 맞추는데 채점하면 런타임 에러가 난다. 2019-06-11 일단 두고 다른 문제 풀러 갑니다. 총총
# https://algospot.com/judge/problem/read/QUADTREE

def calc_end(tree, i):
    '''
    2019-06-11 오후 4시: min 을 사용하도록 수정해도 런타임 오류는 계속 발생... 어디가 원인일까
    '''
    max_index = len(tree)
    end = min(i + 4, max_index)
    while i < end:
        if tree[i] == 'x':
            end = min(end + 4, max_index)
        i += 1
    return i


def calc_half(tree, i):
    max_index = len(tree)
    half = min(i + 2, max_index)
    while i < half:
        if tree[i] == 'x':
            half = min(half + 4, max_index)
        i += 1
    return i


def flip(tree):
    left = []
    right = []
    i = 1
    half = calc_half(tree, i)
    end = calc_end(tree, i)

    # left 를 뒤집어 나간다.
    while i < half:
        if tree[i] == 'x':
            cur_end = calc_end(tree, i+1)
            left.append(flip(tree[i:cur_end]))
            i = cur_end
        else:
            left.append(tree[i])
            i += 1

    while i < end:
        if tree[i] == 'x':
            cur_end = calc_end(tree, i+1)
            right.append(flip(tree[i:cur_end]))
            i = cur_end
        else:
            right.append(tree[i])
            i += 1

    return 'x{}{}'.format(''.join(right), ''.join(left))

cases = int(input())
results = []

for _ in range(cases):
    this_case = input()
    if this_case[0] != 'x':
        results.append(this_case)
        continue
    results.append(flip(this_case))

for elem in results:
    print(elem)

# # len('''
# xwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwxwwwb
# ''')
