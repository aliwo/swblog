from itertools import permutations

'''
정확성  테스트
테스트 1 〉	통과 (0.28ms, 11MB)
테스트 2 〉	통과 (1043.24ms, 16.2MB)
테스트 3 〉	통과 (0.07ms, 10.9MB)
테스트 4 〉	통과 (21.10ms, 13.2MB)
테스트 5 〉	통과 (137.14ms, 35.9MB)
테스트 6 〉	통과 (0.07ms, 11MB)
테스트 7 〉	통과 (0.26ms, 10.9MB)
테스트 8 〉	통과 (249.15ms, 52.3MB)
테스트 9 〉	통과 (0.11ms, 10.9MB)
테스트 10 〉	통과 (1165.23ms, 18.7MB)
테스트 11 〉	통과 (33.33ms, 11.8MB)
테스트 12 〉	통과 (8.60ms, 11.3MB)
'''


def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]


def solution(numbers):
    answer = 0
    perms = set([int(''.join(perm)) for i in range(1, len(numbers) + 1) for perm in permutations(numbers, i)])
    primes = rwh_primes1(max(perms)+1)

    for perm in perms:
        if perm in primes:
            answer+=1

    return answer

print(solution('17'))
print(solution('011'))
