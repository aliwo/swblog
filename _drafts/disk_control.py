from queue import PriorityQueue

def solution(jobs):
    '''
    큐에 들어갈 때에는 (소요시간, 요청시각)
    jobs 의 각 요소는 (요청시각, 소요시간)

    작업을 종료한 시점에서 우선 순위 큐에 들어온 작업 중
    가장 빨리 끝나는 작업을 선택하면 된다.
    -> 작업 시간은 변하지 않기 때문에 대기 시간을 가장 줄일 수 있는 방법은 빨리 끝나는 순서대로 처리하는 것.
    '''
    end = 0
    p_que = PriorityQueue(maxsize=500)
    jobs.sort()

    i = 0
    while i < len(jobs) - 1:

        while True:
            if jobs[i][0] < end: # answer 를 확장해 가며 queue 에 집어 넣는다.
                p_que.put((jobs[i][1], jobs[i][0]))
                elem = p_que.get() # 현재 가장 빨리 끝나는 작업을 저장해 둠.
                end = min(end, jobs[i][1]+elem[0])
                i += 1
            else:
                break

        # 전부 소모.
        while not p_que.empty():
            end += (-p_que.get()[1])





print(solution([[0, 3], [1, 9], [2, 6]])) # 9
