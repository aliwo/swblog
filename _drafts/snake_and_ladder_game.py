# https://www.acmicpc.net/problem/16928

# 사다리와 뱀의 수는 합쳐서 30 까지 올라간다. 탐색할 때는 게임판을 탐색하는게 빠르다.

game_field = [0] * 101 # 0부터 100 까지의 판. 0번 칸은 버린다.
# 0이면 일반 칸, 숫자가 있으면 뱀이나 사다리라는 뜻.

# 사다리와 뱀 입력
ladder_str, snake_str = input().split()

for i in range(0, int(ladder_str) + int(snake_str)):
    info = input().split()
    game_field[int(info[0])] = int(info[1])

# print(game_field)

class Route:

    def __init__(self, cur_pos=1, last_ladder_start=0):
        self.cur_pos = cur_pos
        self.last_ladder_start = last_ladder_start


    def run(self):
        '''
        전방 1에서 6번째 칸을 탐색하고, 사다리를 만나거나, 뱀을 만나면 자기 자신을 복제 합니다.
        cur_pos 가 100 이 되면 현재 loop_run 을 출력하고 프로그램을 종료합니다.
        '''
        far_found = False # 주사위를 써서 가장 멀리까지 가기 위하여
        far = self.cur_pos
        for i in range(min(self.cur_pos+6, 100), self.cur_pos, -1):
            if far_found is False and game_field[i] == 0:
                far_found = True
                far = i
            if game_field[i] != 0: # 뱀이나 사다리인 경우
                if game_field[i] > i: # 사다리
                    self.copy(cur_pos=game_field[i], last_ladder_start=self.cur_pos+i)
                else: # 뱀인 경우
                    self.copy(cur_pos=game_field[i], last_ladder_start=self.last_ladder_start)

        if far_found:
            self.cur_pos = far

        if self.cur_pos == 100:
            print(loop_run) # 전역변수 loop_run 참조
            exit()

    def copy(self, cur_pos, last_ladder_start):
        # 자기 자신을 복사합니다.
        event_loop.append(Route(cur_pos=cur_pos, last_ladder_start=last_ladder_start))

loop_run = 0  # 주사위를 몇 번 굴렸는지
event_loop = [Route()]


while(True):
    loop_run += 1
    for route in event_loop[:]: # event loop 를 run 중에 수정하기 때문에 복사를 써야 합니다.
        route.run()





