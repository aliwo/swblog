from collections import deque


class Branch:

    def __init__(self, q1_sum: int, q2_sum: int, q1_i: int, q2_i: int, attempt: int):
        self.q1_sum = q1_sum
        self.q1_i = q1_i
        self.q2_sum = q2_sum
        self.q2_i = q2_i
        self.attempt = attempt

    def is_even(self) -> bool:
        return self.q1_sum == self.q2_sum


def solution(queue1, queue2):
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)

    if sum_q1 == sum_q2:
        return 0


    branches = deque(
        [
            Branch(  # 1에서 뽑아서 2에 넣는다.
                q1_sum=sum_q1 - queue1[0],
                q1_i=1,
                q2_sum=sum_q2 + queue1[0],
                q2_i=0,
                attempt=1,
            ),
            Branch(  # 2에서 뽑아서 1에 넣는다.
                q1_sum=sum_q1 + queue2[0],
                q1_i=0,
                q2_sum=sum_q2 - queue2[0],
                q2_i=1,
                attempt=1,
            )
        ]
    )

    for branch in branches:
        if branch.is_even():
            return branch.attempt

    del sum_q1, sum_q2

    while branches:
        branch = branches.popleft()
        if branch.q1_i < len(queue1):
            # 1에서 뽑아서 2에 넣는 경우
            q1_sum1 = branch.q1_sum - queue1[branch.q1_i]
            q2_sum1 = branch.q2_sum + queue1[branch.q1_i]

            if q1_sum1 == q2_sum1:
                return branch.attempt + 1

            branches.append(
                Branch(
                    q1_sum=q1_sum1,
                    q1_i=branch.q1_i + 1,
                    q2_sum=q2_sum1,
                    q2_i=branch.q2_i,
                    attempt=branch.attempt + 1,
                )
            )
        if branch.q2_i < len(queue2):
            # 2에서 뽑아서 1에 넣는 경우
            q1_sum2 = branch.q1_sum + queue2[branch.q2_i]
            q2_sum2 = branch.q2_sum - queue2[branch.q2_i]

            if q1_sum2 == q2_sum2:
                return branch.attempt + 1

            branches.append(
                Branch(
                    q1_sum=q1_sum2,
                    q1_i=branch.q1_i,
                    q2_sum=q2_sum2,
                    q2_i=branch.q2_i + 1,
                    attempt=branch.attempt + 1,
                )
            )


    return -1


# print(solution([3, 2, 7, 2], [4, 6, 5, 1])) # 	2
print(solution([1, 2, 1, 2], [1, 10, 1, 2])) #	7
# solution([1, 1], [1, 5]) #	-1
