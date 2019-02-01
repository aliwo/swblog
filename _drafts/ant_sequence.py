

def next_ant_seq(prev_seq):
    result = []
    target = prev_seq[0]
    cnt = 0
    for char in prev_seq:
        if char == target:
            cnt += 1
        else:
            result.append('{}{}'.format(target, cnt))
            target = char
            cnt = 1
    result.append('{}{}'.format(target, cnt))

    return ''.join(result)

def solution(A):
    answer = '1'
    for a in range(A-1):
        answer = next_ant_seq(answer)

    return answer


print(solution(40))



