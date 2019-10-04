from queue import PriorityQueue




def solution(jobs):
    '''
    채점 시간을 보니 최소 n log n 안에는 끝나야 한다.

    for 문이 한 번 회전 할 때 마다
    job 은 종료되어야 한다. 로직을 정리하면 다음과 같다.


    1. 큐에서 새로운 작업을 뽑아낸다.
    2. 큐에 아무것도 없으면??
    job 의 실행 중에 n 개의 새로운 작업이 들어온다.
    n 개의 작업은 큐에 추가.

    마지막 job 의 실행 중에는 새로운 작업이 들어오지 않는다.

    '''
    answer = 0
    p_que = PriorityQueue(maxsize=500)
    jobs.sort()

    i = 0
    for job in jobs:
        pass

    return answer / len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]])) # 9
