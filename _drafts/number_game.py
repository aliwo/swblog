import heapq

'''
정확성  테스트
테스트 1 〉	통과 (0.06ms, 10.7MB)
테스트 2 〉	통과 (0.04ms, 10.7MB)
테스트 3 〉	통과 (0.04ms, 10.7MB)
테스트 4 〉	통과 (0.04ms, 10.7MB)
테스트 5 〉	통과 (0.06ms, 10.7MB)
테스트 6 〉	통과 (0.08ms, 10.6MB)
테스트 7 〉	통과 (0.07ms, 10.6MB)
테스트 8 〉	통과 (0.07ms, 10.7MB)
테스트 9 〉	통과 (0.51ms, 10.9MB)
테스트 10 〉	통과 (0.38ms, 10.7MB)
테스트 11 〉	통과 (0.56ms, 10.9MB)
테스트 12 〉	통과 (0.28ms, 10.8MB)
테스트 13 〉	통과 (3.88ms, 15.3MB)
테스트 14 〉	통과 (6.42ms, 20MB)
테스트 15 〉	통과 (4.28ms, 15.8MB)
테스트 16 〉	통과 (5.89ms, 19.2MB)
테스트 17 〉	통과 (1.06ms, 11.1MB)
테스트 18 〉	통과 (1.16ms, 13MB)
효율성  테스트
테스트 1 〉	통과 (115.94ms, 162MB)
테스트 2 〉	통과 (110.83ms, 157MB)
테스트 3 〉	통과 (120.74ms, 158MB)
'''

# 단순 정렬 보다 힙이 훨씬 빠르다. 단순 리스트 정렬의 성능:
# 효율성  테스트
# 테스트 1 〉	통과 (1751.05ms, 164MB)
# 테스트 2 〉	통과 (1638.94ms, 157MB)
# 테스트 3 〉	통과 (811.98ms, 158MB)

def solution(A, B):
    cnt = 0
    heapq.heapify(A)
    heapq.heapify(B)

    while A and B:
        a = heapq.heappop(A)
        b = heapq.heappop(B)
        while a > b:
            if B:
                b = heapq.heappop(B)
            else:
                return cnt
        cnt += 1

    return cnt


print(solution([5,1,3,7], [2,2,6,8]))
print(solution([5,1,3,7,5], [2,2,6,8,5])) # 4
print(solution([2,2,2,2], [1,1,1,1]))
