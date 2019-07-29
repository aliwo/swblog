cases = int(input())
maxs = []
for i in range(cases):
    nums = [int(x) for x in input().split()]
    maxs.append(max(nums))

for i in range(len(maxs)):
    print('#{} {}'.format(i + 1, maxs[i]))



