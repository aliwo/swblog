cache = {}

def fib(n):
    if n <= 2:
        return 1
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

def solution(N):
    edge1 = fib(N)
    edge2 = edge1 + fib(N-1)
    return 2 * (edge1 + edge2)

'''
정확성  테스트
테스트 1 〉	통과 (0.04ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (0.03ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.7MB)
테스트 5 〉	통과 (0.05ms, 10.7MB)
테스트 6 〉	통과 (0.04ms, 10.7MB)
테스트 7 〉	통과 (0.04ms, 10.7MB)
테스트 8 〉	통과 (0.05ms, 10.7MB)
효율성  테스트
테스트 1 〉	통과 (0.07ms, 10.8MB)
테스트 2 〉	통과 (0.07ms, 10.8MB)
테스트 3 〉	통과 (0.08ms, 10.7MB)
테스트 4 〉	통과 (0.07ms, 10.7MB)
'''

def solution(N):
    '''
    재귀호출도 안하고 코드도 단순해서
    재귀 호출을 사용한 DP 보다도 빠르다... ㅎㄷㄷ
    '''
    l=[1,1]
    for i in range(2,N):
        l.append(l[-1]+l[-2])
    answer = (l[-1]*2+l[-2])*2
    return answer

'''
정확성  테스트
테스트 1 〉	통과 (0.03ms, 10.6MB)
테스트 2 〉	통과 (0.03ms, 10.8MB)
테스트 3 〉	통과 (0.03ms, 10.6MB)
테스트 4 〉	통과 (0.04ms, 10.7MB)
테스트 5 〉	통과 (0.04ms, 10.7MB)
테스트 6 〉	통과 (0.04ms, 10.7MB)
테스트 7 〉	통과 (0.04ms, 10.7MB)
테스트 8 〉	통과 (0.04ms, 10.8MB)
효율성  테스트
테스트 1 〉	통과 (0.05ms, 10.8MB)
테스트 2 〉	통과 (0.05ms, 10.7MB)
테스트 3 〉	통과 (0.04ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.7MB)
'''

print(solution(1))
