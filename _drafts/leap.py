cache = {}

def solution(n):
    def sol(n):
        if n in cache:
            return cache[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        cache[n] = sol(n - 1) + sol(n - 2)

        return cache[n]

    return sol(n) % 1234567

def solution(n):
    m = [1,2]
    if n <= 2:
        return m[n-1]

    for i in range(3, n+1):
        m.append(m[-1] + m[-2])
    return m[n-1] %1234567

def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b

def solution(n):
    if n == 1:
        return 1
    return jumpCase(n) % 1234567

print(solution(1234567))
