def solution(A):
    '''
    A 는 정렬되어 있지 않다. 따라서 빠진 숫자를 찾으려면
    리스트의 모든 요소를 한 번은 봐야 한다.
    최소 O(N) 의 시간 복잡도가 필요하다는 말.

    정렬 -> zip(range(1, N+2), A) 를 사용하느냐
    (N log N) + N

    1 ~ N+1 까지를 갖고 있는 집합을 만든 후, 집합에서 지워 나가느냐
     -> 2 N 의 시간 복잡도

    '''

    pass