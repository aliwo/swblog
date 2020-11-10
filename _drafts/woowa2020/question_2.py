
op_dict = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}


def solution(s, op):
    '''
    s의 길이는 2 이상 10 이하
    '''
    return [op_dict[op](int(s[:i]), int(s[i:])) for i in range(1, len(s))]


# print(solution("1234", '+'))
# print(solution("987987", '-'))
# print(solution("31402", '*'))
print(solution("12", '*'))