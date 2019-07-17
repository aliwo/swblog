def solution(s):
    words = s.split()
    results = []
    for word in words:
        result = []
        for i, char in enumerate(word):
            if i % 2 == 0: # 짝수라면
                result.append(str.upper(char))
            else:
                result.append(str.lower(char))
        results.append(''.join(result))


    return ' '.join(results)


def assert_solution():
    assert solution('try hello world') == 'TrY HeLlO WoRlD'
    assert solution('this is KIMCHI') == 'ThIs Is KiMcHi'
    assert solution('this  is KIMCHI') == 'ThIs Is KiMcHi'
    assert solution('this is KIMCHI000') == 'ThIs Is KiMcHi000'
    assert solution('this is KIMCHI000안녕') == 'ThIs Is KiMcHi000안녕'
    assert solution('t') == 'T'
    assert solution('T') == 'T'

assert_solution()
