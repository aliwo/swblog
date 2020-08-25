
strategy = '''
현재 진행 방향에서 막다른 곳에 도달했을 때 '오른쪽' 으로 틀 수 없다면 종료한다.
혹은 result 의 길이가 n * m 이 되면 종료한다.
오른쪽 진행: j를 증가 시킨다. turn 할 때는 i를 증가시킨다.
아래쪽 진행: i를 증가 시킨다. turn 할 때는 j를 감소시킨다.
왼쪽 진행: j를 감소 시킨다. turn 할 때는 i를 감소시킨다.
'''

class Mover:

    def __init__(self, array):
        self.array = array
        self.direction = ['r', 'd', 'l', 'u'] # right down left up
        self.cur = 0
        self.i = 0
        self.j = 0
        self.result = []
        self.step = set()

    def turn(self):
        self.cur = self.cur + 1 if self.cur + 1 < len(self.direction) else 0

    def stuck(self):
        if self.i >= len(self.array) or self.i < 0:
            return True
        if self.j >= len(self.array[self.i]) or self.j < 0:
            return True
        if f'{self.i}{self.j}' in self.step:
            return True

    def move(self):
        self.step.add(f'{self.i}{self.j}')
        self.result.append(self.array[self.i][self.j])
        if self.direction[self.cur] == 'r':
            self.j += 1
            if self.stuck():
                self.j -= 1
                self.turn()
                self.i += 1
        elif self.direction[self.cur] == 'd':
            self.i += 1
            if self.stuck():
                self.i -= 1
                self.turn()
                self.j -= 1
        elif self.direction[self.cur] == 'l':
            self.j -= 1
            if self.stuck():
                self.j += 1
                self.turn()
                self.i -= 1
        elif self.direction[self.cur] == 'u':
            self.i -= 1
            if self.stuck():
                self.i += 1
                self.turn()
                self.j += 1



def spiral_traverse(array):
    elements_cnt = len(array) * len(array[0])
    mover = Mover(array)
    while len(mover.result) < elements_cnt:
        mover.move()
        print(mover.result, mover.direction[mover.cur])
    return mover.result



array = [
    [1,2,3,4],
    [12,13,14,5],
    [11,16,15,6],
    [10,9,8,7],
]
print(spiral_traverse(array))


