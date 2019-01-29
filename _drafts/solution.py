
def has_intersect(a, b):
    '''

    :param a: 바깥 enumerate 에서 구한 오른쪽 반원의 튜플 (중심, 오른쪽 끝) 의 오른쪽 끝
    :param b: 내부 enumerate 에서 구한 전체 원 (왼쪽 끝, 오른쪽 끝) 왼쪽 끝
    :return:
    '''
    if b <= a:
        return True
    return False

def solution(A):
    '''
    :param A: 원의 반지름이 적힌 리스트
    :returns 겹치는 원의 개수
    '''
    cnt = 0
    for index, radius in enumerate(A):
        for index_2, radius_2 in enumerate(A):
            if index_2 <= index:
                continue
            if has_intersect(index+radius, index_2-radius_2):
                cnt +=1

    if cnt > 10000000:
        return -1

    return cnt

print(solution([1, 5, 2, 1, 4, 0]))





#
# def solution(A):
#     '''
#     :param A: 원의 반지름이 적힌 리스트
#     :returns 겹치는 원의 개수
#
#     TODO: 너무 오래 걸릴 삘임 ㅎㅎ 병목은 어디인가?
#     TODO: set 으로 만들지 말고 range 혹은 tuple 상태에서 교차점 발견하면 바로 True 리턴하도록 하기
#     '''
#     cnt = 0
#     for index, radius in enumerate(A):
#         cur_range = range(index, index+radius+1)
#         for index_2, radius_2 in enumerate(A):
#             if index_2 <= index:
#                 continue
#             if len(set(cur_range).intersection(range(index_2-radius_2, index_2+radius_2+1))) > 0:
#                 cnt +=1
#
#     if cnt > 10000000:
#         return -1
#
#     return cnt
#
# print(solution([1, 5, 2, 1, 4, 0]))



