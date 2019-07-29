# https://programmers.co.kr/learn/courses/30/lessons/42586
import math

def solution(progresses, speeds):
    cache = [] # 우선순위 대로 넣는 스택. [et, 개수]를 저장합니다.

    for i in range(len(progresses)):
        et = math.ceil((100 - progresses[i]) / speeds[i])

        if not cache:
            cache.append([et, 1])
            continue

        if et > cache[-1][0]:
            cache.append([et, 1])
            continue
        else:
            cache[-1][1] += 1

    return [i[1] for i in cache]
