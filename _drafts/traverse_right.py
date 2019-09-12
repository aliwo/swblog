
done = [True]
done2 = [True, True]
done3 = [True, False]
done4 = [True, False, False]
done5 = [True, False, True, True, True, False, False]
done6 = [False, False, True, True, True, False, True]


def traverse_right(done, i):
    cnt = 0

    for _ in range(len(done)):
        if done[i] == False:
            break
        i = i + 1 if i + 1 < len(done) else 0
        cnt += 1

    if cnt == len(done): # 못 찾았다는 뜻
        return 0

    done[i] = True
    cnt += traverse_right(done, i)
    done[i] = False
    return cnt


def traverse_left(done, i):
    cnt = 0

    for _ in range(len(done)):
        if done[i] == False:
            break
        i = i - 1 if i > 0 else len(done) - 1
        cnt += 1

    if cnt == len(done): # 못 찾았다는 뜻
        return 0

    done[i] = True
    cnt += traverse_left(done, i)
    done[i] = False
    return cnt


def traverse(done, i):
    # TODO ; left_cnt 보다 right_cnt 가 크면 right 탐색을 중단 하는 최적화가 가능할까? 답에 영향이 없을까?

    # 기저 사례
    if False not in done:
        return 0

    left_cnt = right_cnt = 0
    left_i = right_i = i

    for _ in range(len(done)):
        if done[left_i] == False:
            break
        left_i = left_i - 1 if left_i > 0 else len(done) - 1
        left_cnt += 1
    done[left_i] = True
    left_cnt += traverse(done, left_i)
    done[left_i] = False

    for _ in range(len(done)):
        if done[right_i] == False:
            break
        right_i = right_i + 1 if right_i + 1 < len(done) else 0
        right_cnt += 1
    done[right_i] = True
    right_cnt += traverse(done, right_i)
    done[right_i] = False

    return min(left_cnt, right_cnt)

print(traverse(done5, 0))
print(traverse(done6, 0))


# # print(traverse_left(done5, 0)) # 6
# print(traverse_left(done6, 0)) # 6
# print(done6)
# print(traverse_left(done6, 1)) # 3
# print(traverse_right(done6, 0))
# print(traverse_right(done6, 1))

# TODO: 멀쩡한 traverse left 와 right 는 만들었다... 이제 잘 활용해서 양방향 traverse 를 만들면 된다.
