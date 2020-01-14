
def solution(S):
    '''
    문자열을 S, 글자의 길이를 L 이라 하자.
    글자 하나를 제거했을 때 발생하는 효과는 다음 두가지 중 하나이다.
    ->    index 0 ~ L-2 사이의 글자를 제거했을 때: 바로 뒤 글자로 대체된다.
    ->    index L-1 의 글자를 제거했을 때: 자기만 없어진다.

    일반적으로 인덱스가 낮은 글자를 제거했을 때 alphabetically small 해 지지만...
    인덱스가 낮은 곳에서 a 를 b 로 바꾸는 것 보다, 인덱스가 높은 곳에서 z 를 a 로 바꾸는게 낫다.

    '''
    result = []
    for i in range(len(S)-1):
        if ord(S[i]) > ord(S[i+1]):
            # print(f'{S[i]}: {ord(S[i])}      {S[i+1]}: {ord(S[i+1])}')
            result.append(S[:i] + S[i+1:])
    result.append(S[:-1])
    return sorted(result)[0]


# print(solution('acb'))
# print(solution('abc'))
# print(solution('bca'))
print(solution('cba'))
print(solution('cab'))
print(solution('codility'))
print(solution('aaaa'))
print(solution('kimchi'))
print(solution('yogiyo'))
print(solution('aaab'))
print(solution('baza'))
print(solution('hot')) # 어짜피 하나는 빼야 하는데, 아무것도 기준에 충족하지 않으면, 마지막을 빼야 함.

