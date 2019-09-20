
done = [True, False, False, False]
done2 = [True, False, True, True, True, False, False] # ABAAABB 의 최적해는 7(이동 4)

# def turn_left(done, i):
#     left = i
#     cnt = 0
#     for _ in range((len(done) // 2) + 1):
#         left = left - 1 if left > 0 else len(done) - 1
#         cnt += 1
#         if done[left] == False:
#             done[left] = True
#             result = cnt + alter_cursor(done, left)
#             done[left] = False
#             return result
#     return 0
#
#
# def turn_right(done, i):
#     right = i
#     cnt = 0
#     for _ in range((len(done) // 2) + 1):
#         right = right + 1 if right < len(done) - 1 else 0
#         cnt += 1
#         if done[right] == False:
#             done[right] = True
#             result = cnt + alter_cursor(done, right)
#             done[right] = False
#             return result
#     return 0


def alter_cursor(done, i):
    '''
    특정 지점에서
    bool 리스트 done 의 모든 False 를 한 번 씩 방문하기 위한
    가장 효율적인 이동, 그 이동 횟수를 구합니다.

    [True, True, True], 0 -> 0
    [True, False, True], 0 -> 1
    [True, True, False], 0 -> 1
    [True, False, False], 0 -> 2
    '''
    left = right = i
    result = 9999999

    if False not in done:
        return 0

    cnt = 0
    for _ in range((len(done) // 2) + 1):
        left = left - 1 if left > 0 else len(done) - 1
        cnt += 1
        if done[left] == False:
            done[left] = True
            result = min(result, cnt + alter_cursor(done, left))
            done[left] = False

    cnt = 0
    for _ in range((len(done) // 2) + 1):
        right = right + 1 if right < len(done) - 1 else 0
        cnt += 1
        if done[right] == False:
            done[right] = True
            result = min(result, cnt + alter_cursor(done, right))
            done[right] = False

    return min(left, right)


# print(alter_cursor([True, True, True], 0))
# print(alter_cursor([True, False, True], 0))
# print(alter_cursor([True, True, False], 0))
# print(alter_cursor([True, False, False], 0))
# print(alter_cursor(done, 0))
print(alter_cursor(done2, 0))

