from typing import List, Any


class Branch:
    """
    상인이 하루에 선택할 수 있는 경우의 수 입니다.
    상인은 매일...
        - 구매
        - 가만히 있거
        - 판매
    를 할 수 있습니다.
    """

    def __init__(self, money: int, stone: int):
        self.money = money
        self.stone = stone

    def buy(self, price: int) -> "Branch":
        """
        하루에 1 개만 살 수 있습니다.
        예외: 돈이 모자랄 경우 stay 합니다.
        """
        if self.money >= price:
            return Branch(
                money=self.money - price,
                stone=self.stone + 1,
            )
        return self.stay(price)

    def stay(self, price: int) -> "Branch":
        """
        사지 않고 가만히 있습니다.
        예외: 시세가 0원이라고요? 그러면 가만히 있을 수 없죠!
        """
        if price == 0:
            return self.buy(price)
        return self

    def sell(self, price: int, stone: int) -> "Branch":
        """
        price 가격에 stone 개수 만큼 판매 합니다.
        예외:
            - 가격이 0원인 경우 팔지 않고 바로 삽니다.
            - 돌이 부족한 경우 가만히 있습니다.
        """
        if price == 0:
            return self.buy(price)

        if self.stone >= stone:
            return Branch(
                money=self.money + (price * stone),
                stone=self.stone - stone,
            )
        return self.stay(price)

    def __hash__(self) -> int:
        return hash(f'{self.money}_{self.stone}')

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Branch) and self.money == other.money and self.stone == other.stone

    def __gt__(self, other) -> bool:
        return isinstance(other, Branch) and self.money > other.money

    def __ge__(self, other) -> bool:
        return isinstance(other, Branch) and self.money >= other.money

    def __lt__(self, other) -> bool:
        return isinstance(other, Branch) and self.money < other.money

    def __le__(self, other) -> bool:
        return isinstance(other, Branch) and self.money <= other.money


def solution(n: int, price: List[int]) -> int:
    """
    branches 는 상인이 하루 동안 취할 수 있는 행동의 모든 경우의 수를 담고 있습니다.

    for loop 한 번 회전이 곧 하루를 의미 합니다.
    하루 동안 상인은
        - branch.stay() 가만하 있거나
        - branch,buy() 돌을 사거나
        - 아니면 자신이 가지고 있는 돌 만큼 range(1, branch.stone + 1)
          판매를 할 수 있습니다.

    """
    branches = [
        Branch(money=0, stone=0)
    ]

    for i in range(price.index(0), len(price)):
        new_branches = []
        while branches:
            branch = branches.pop()
            branch_set = {branch.stay(price[i]), branch.buy(price[i])}
            for stone in range(1, branch.stone + 1):
                branch_set.add(branch.sell(price[i], stone))

            for branch in branch_set:
                new_branches.append(branch)

        branches = new_branches


    return max(branches).money


print(solution(2, [0,1,2]) == 2)
print(solution(2, [0,0,3,1,1,1,9]) == 36)

print(solution(2, [1,0,0]) == 0)
print(solution(2, [0,0,1,1,9]) == 18)


# 시세가 0인 날에 처음 으로 돌을 1개 살 수 있음.
# 그 다음 시세가 0이 아닌 날에 팔 수 있음.


# 매 번 다음의 선택지가 존재
# 가만히 있는다.
# 산다. (돈이 있을 때)
# 판다. (돌이 있을 때)


# 0원에 사서 9원에 팔고 가만히 있는다.
# [0, 9, 1, 1, 1] -> 9
# [0, 1, 1, 1, 9] -> 9
# 0원에 사고 9원에 팔고, 나머지는 가만히 있는다.


# 가장 시세가 비싼 날에 팔면 안 되는 경우
# [0, 9, 9, 1, 8, 1, 8]


# 리스트 길이는 100... 완전 탐색해도 되겠는데?
