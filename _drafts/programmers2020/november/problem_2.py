def solution(s):
    total_zero_cnt = 0
    conversion_cnt = 0
    while s != '1':
        zero_cnt = 0
        one_cnt = 0
        for char in s:
            if char == '0':
                zero_cnt += 1
            else:
                one_cnt += 1
        s = "{0:b}".format(one_cnt)
        total_zero_cnt += zero_cnt
        conversion_cnt += 1
    return [conversion_cnt, total_zero_cnt]

print(solution("110010101001"))