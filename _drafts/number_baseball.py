
# 가설 1: 0 스트라이크 0 볼이 나오면 제대로 계산하지 못한다.
# -> 반론: 모든 질문이 0스트라이크 0볼이 아닌 이상 xxx 는 소거 된다.

# 가설 2: 설마 질문에는 0이 들어갈까?
# -> 0 없애도록 했는데 역시 오답...

# 사실은 111 처럼 중복이 가능하다? -> 문제에 명시되어 있다. 중복은 없어.



def strikes(elem):
    if elem[1] == 0:
        return ['xxx']
    question = str(elem[0])
    if elem[1] == 1:
        return [f'{question[0]}xx', f'x{question[1]}x', f'xx{question[2]}']
    if elem[1] == 2:
        return [f'{question[0]}{question[1]}x', f'x{question[1]}{question[2]}', f'{question[0]}x{question[2]}']
    return [question]


def balls(elem):
    if elem[2] == 0:
        return ['xxx']
    question = str(elem[0])
    if elem[2] == 1:
        return [f'x{question[0]}x', f'xx{question[0]}', f'{question[1]}xx', f'xx{question[1]}',
                f'{question[2]}xx', f'x{question[2]}x']
    if elem[2] == 2:
        return [
            f'{question[1]}{question[0]}x', f'{question[1]}x{question[0]}', f'x{question[0]}{question[1]}'
            ,f'{question[1]}{question[2]}x', f'x{question[2]}{question[1]}', f'{question[2]}x{question[1]}'
            ,f'{question[2]}x{question[0]}', f'{question[2]}{question[0]}x', f'x{question[2]}{question[0]}'
                ]
    return [f'{question[1]}{question[2]}{question[0]}', f'{question[2]}{question[0]}{question[1]}']


def intersect(poss1, poss2):
    '''
    배열 poss1 과 poss2 를 비교했을 때 가능한 모든 조합을 리턴합니다.
    '''
    possibilities = []
    for elem in poss1:
        for elem2 in poss2:
            temp = []
            for ch1, ch2 in zip(elem, elem2):
                if ch1 == '0' or ch2 == '0':
                    break
                if ch1 == 'x' and ch2 == 'x':
                    temp.append('x')
                elif ch1 == 'x' and ch2 not in temp:
                    temp.append(ch2)
                elif ch2 == 'x' and ch1 not in temp:
                    temp.append(ch1)
                elif ch1 == ch2 and ch1 not in temp:
                    temp.append(ch1)
                else:
                    break
            else:
                possibilities.append(''.join(temp))
    return possibilities


def form_possibilities(poss):
    '''
    주어진 숫자와, 스트라이크, 볼의 수로 가능한 모든 조합을 리턴합니다.
    스트라이크로 얻을 수 있는 모든 조합과, 볼로 얻을수 있는 모든 조합을 인터섹트 하면 나옵니다.
    '''
    return intersect(strikes(poss), balls(poss))


def solution(baseball):
    # 첫번째 질문으로 possibilities 생성
    possibilities = form_possibilities(baseball[0])

    for elem in baseball[1:]:
        possibilities = intersect(possibilities, form_possibilities(elem))

    return len(set(possibilities))

# print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
# print(solution([[156, 0, 0], [123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
print(solution([[156, 0, 0], [123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1], [624, 2, 0]])) # 답이 하나로 줄음... 무섭도록 완벽하게 동작하네

print(solution([[127, 3, 0]])) # 789

