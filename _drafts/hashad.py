def solution(x):
    str_x = str(x)
    sum_ = sum([int(x) for x in str_x])
    return x % sum_ == 0
