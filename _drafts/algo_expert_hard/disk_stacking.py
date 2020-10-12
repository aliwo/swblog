
# 와 어렵네...
# width, depth, height 은 규칙이 없으니까. 이것도 DP 인거 같고
# 높이를 리턴하는게 아니라 쌓은 stack 자체를 리턴해야 한다.

strategy = '''
내 접근 방식 (디스크를 거꾸로 쌓는다.)
1. 각 disk 로 부터 시작하는 stack 을 stacks 에 저장.
2. stacks 가 다 없어질 때 까지 while 회전
3. 각 stack 마다 추가할 disk 가 있다면 disk 를 추가한 뒤 new_stacks 에 담는다.
4. 추가할 disk 가 하나도 없는 stack 은 new_stack 에 못 들어간다. max_height 를 산출한다. 
5. 새로운 max_height 가 나왔다면 max_height 를 업데이트
6. stack = new_stack

최악의 경우의 수의 시간복잡도는...?
하나의 스택이 n ((n-1) + (n-2) + (n-3) ... 1) 의 가지를 만들어 낼 때. 즉 n^2 이네...
처음에 n 개의 스택으로 시작하니까 n^3 이군.
'''

def diskStacking(disks):
    stacks = [[disk] for disk in disks]
    max_height = 0
    max_stack = []
    while stacks:
        new_stacks = []
        # 모든 disk 를 다 돌았는데도 추가할 disk 가 없으면 해당 stack 은 끝났다.
        for i, stack in enumerate(stacks):
            for disk in disks:
                # 어짜피 같은 stack 은 크기 문제로 두 번 못 고른다.
                if stack[-1][0] < disk[0] and stack[-1][1] < disk[1] and stack[-1][2] < disk[2]:
                    new_stack = stack[:]
                    new_stack.append(disk)
                    new_stacks.append(new_stack)
            else:
                height = 0
                for d in stack:
                    height += d[2]
                # height = reduce(lambda x, y: x[2] + y[2], stack) if len(stack) < 1 else stack[-1][2]
                if max_height < height:
                    max_height = height
                    max_stack = stack
        stacks = new_stacks
    return max_stack

print(diskStacking([[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]))


