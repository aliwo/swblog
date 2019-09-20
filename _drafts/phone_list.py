
# 느리지만 반드시 정답을 리턴하는 방법
def solution(phone_book):
    '''
    처음에 dict 에 모든 key 를 넣고 검사하는 방법은? 너무 느릴걸.
    '''
    cache = {}

    for elem in phone_book:
        for i in range(1, len(elem) + 1):
            if elem[0:i] in cache:
                return False
        cache[elem] = 1
    return True


# 정렬을 안 쓰는 솔루션
# 해쉬도 안 쓴다.
def solution(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i] # 현재 요소
        for j in range(i+1, len(phone_book)): # phone_book 의 나머지 요소
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True


assert solution(["119", "97674223", "1195524421"]) == False
# assert solution(["97674223", "1195524421", "119"]) == False
