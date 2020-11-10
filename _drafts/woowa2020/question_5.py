

def solution(penter, pexit, pescape, data):
    answer = []
    for i in range(0, len(data), len(penter)):
        cur_data = data[i:i+len(penter)]
        if cur_data in [penter, pexit, pescape]:
            answer.append(f'{pescape}{cur_data}')
        else:
            answer.append(cur_data)
    return f'{penter}{"".join(answer)}{pexit}'

assert "110011011001100110010010111100111001110000000010" == solution('1100', '0010', '1001',"1101100100101111001111000000")
# assert "100000010010001111" == solution("10", '11', '00',"00011011")



