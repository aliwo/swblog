
# 2019-10-21 한 문제를 이틀 사흥을 붙잡는 내 지금의 방식은 효율적이라고 볼 수가 없다.
# 4시간 보고 안 풀리면 던져야 된다. 다른 문제로 넘어가자. (답지를 보기는 싫다)
# 앞으로는 난이도를 좀 낮춰야 겠다고 생각.
# 사흘이 걸려서 한 문제를 풀었을때의 쾌감은 이제 못느끼는 걸까. 좀 아쉽긴 하네.

# word_puzzle 4을 4번째 바리에이션 까지 만들면서 시도했던 방법은 다음과 같다.
# 1. 재귀호출을 이용한 완전탐색
# 2. 반복을 이용한 완전탐색 (오답, 이미 순회했던 요소를 다시 순회하는 문제를 해결하지 못했다.)
# 3. 반복을 이용한 완전탐색. 튜플에 index 를 함께 저장해 반복 Context 를 잃어버리지 않도록 개선 (정답, 그러나 효율성 실패)
# 4. 0 부터 떨어져 있는 거리를 기억하는 방식의 슬라이딩 윈도우. 지금까지의 방법중 가장 빠르나, 효율성 테스트 실패.
#    min 값을 발견하면 바로 리턴하기 때문에 완전탐색과 비교했을 때 훨씬 효율적이다.

# t 가 최대 20000, strs 로 중복 없이 만들 수 있는 가장 긴 단어는 500 이므로 겹치는 단어가 많이 생길 수 있다는 것을
# 발견했다. 메모이제이션을 쓰면 좋겠으나. 마땅한 방법이 생각나지 않아 일단 발견한 사실을 적어만 둔다.


from collections import defaultdict

cache = {}


def match(a, b):
    if len(b) > len(a):
        return False
    for a_char, b_char in zip(a, b):
        if a_char != b_char:
            return False
    return True


def solution(strs, t):
    # str_hash 만들기
    str_hash = defaultdict(lambda: [])
    for word in strs:
        str_hash[word[0]].append(word)

    # cache, cnt, window
    cache = {0 : [len(x) for x in strs if match(t[0: 0 + len(x)], x)]}
    cnt = 1
    window = cache[0]

    while True:
        next_window = set()
        for length in window:

            # 기저 사례. 단어 매칭에 성공한 케이스
            if length == len(t):
                return cnt

            # 다음 윈도우를 만들기 위해 cache 를 형성
            if length not in cache:
                cache[length] = [length + len(x) for x in str_hash[t[length]] if match(t[length: length + len(x)], x)]
            # next_window 에 합친다.
            next_window.update(cache[length])

        if not next_window:
            return -1

        window = next_window
        cnt += 1



print(solution(['ba', 'na', 'n', 'a'], 'banana'))
print(solution(['ba', 'na', 'n', 'a'], 'bababa'))
print(solution(["ba", "an", "nan", "ban", "n"], "banana"))
print(solution(["app", "ap", "p", "l", "e", "ple", "pp"], "apple"))

