def solution(pattern, test_cases):
    '''

    ? 를 처리하는 방법: 한 글자를 무시한다.
    ? 만 처리하는 방법을 작성하는 건 의미가 없다. * 때문에 전혀 다른 방식을 사용해야 한다.


    '''
    answer = []

    for text in test_cases:
        match = True
        for i in range(len(text)):
            if pattern[i] == '?':
                continue # 검사를 하지 않고 넘어간다.
            if pattern[i] != text[i]: # 매칭 실패!
                match = True
                break

        if match:
            answer.append(text)

    answer.sort()
    return answer

assert solution('he?p', ['help', 'heap', 'helpp']) == ['heap', 'help'] # 알파벳 순서대로 출력.


