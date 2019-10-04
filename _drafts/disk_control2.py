# 아무리 느린 방법 이라지만 테스트 20 개 중에서 19개가 시간 초과라니.
# 작업이 최대 1000 개고, 하나당 소요시간은 최대 1000 이니 최대 1000 * 1000 번 회전이다. 따라서 시간초과.

from queue import PriorityQueue


def solution(jobs):
    '''
    결국 포기하고 시간을 가리키는 클록을 지정하기로 했다.
    '''
    p_que = PriorityQueue(maxsize=500)
    jobs.sort()

    total = 0
    answer = 0 # 이번 작업의 종료 시각. 마지막 작업의 종료시간이 바로 답이 된다.
    i = 0 # 현재 시각을 나타내는 클록
    j = 0 # jobs 의 몇 번째 요소까지 집어 넣었는지.
    while j < len(jobs) - 1 or (not p_que.empty()):

        if j < len(jobs) and jobs[j][0] == i: # 현 시점에 요청이 들어오면
            p_que.put((jobs[j][1], jobs[j][0]))
            j += 1

        if answer <= i:
            elem = p_que.get()
            answer += elem[0]
            total += answer - elem[1]

        i += 1

    return total / len(jobs)



print(solution([[0, 3], [1, 9], [2, 6]])) # 9
