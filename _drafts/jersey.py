
def solution(n, lost, reserve):

    losers = lost_len = len(lost)
    i = j = 0

    while True:

        if lost_len == i - 1:
            break

        # 도난 당한 학생이 여분도 가지고 있었는지 체크
        if lost[i] == reserve[j]:
            reserve._pop(j)
            i += 1 # j는 += 1 하지 않는다.

        # 바로 왼쪽에 여분이 있었을 경우
        elif lost[i] - 1 == reserve[j]:
            reserve._pop(j)
            losers -= 1
            i += 1
            j += 1

        elif lost[i] + 1 == reserve[j]:
            reserve._pop(j)
            losers -= 1
            i += 1
            j += 1


    return n - losers


