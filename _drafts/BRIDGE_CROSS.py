import queue
# 다리를 건너고 있다는 걸 어떻게 표현하나? 리스트에서 한 칸씩 밀어?
# 문제에서 '정해진 순으로 건넌다' 고 했기 때문에 truck_weights 는 정렬할 수 없습니다.

class G:
    crossed = [] # 다리를 다 지난 트럭
    crossing = None # queue 가 들어갈 자리
    on_bridge = 0
    time = 0


def solution(bridge_length, weight, truck_weights):
    truck_cnt = len(truck_weights)
    G.crossing = queue.Queue(bridge_length)
    i = 0

    # 기저 사례: 다리 길이가 1 이면 한 대씩 건너면 장땡이다.
    if bridge_length == 1:
        return len(truck_weights) + 1

    while len(G.crossed) < truck_cnt: # 모든 truck 이 건널 때 까지 반복
        while not G.crossing.full(): # 다리가 꽉 찰 때 까지
            if i < truck_cnt and G.on_bridge + truck_weights[i] <= weight:
                G.crossing.put(truck_weights[i])
                G.on_bridge += truck_weights[i]
                i += 1
            else:
                G.crossing.put(0)
            G.time += 1

        # 차를 하나만 빼고, 여유가 있다면 차를 넣는다. 이 2가지 작업은 1 tick 에 일어남.
        cur_truck = G.crossing.get_nowait()
        if cur_truck != 0:
            G.crossed.append(cur_truck)
        G.on_bridge -= cur_truck

        if i < truck_cnt and G.on_bridge + truck_weights[i] <= weight:
            G.crossing.put(truck_weights[i])
            G.on_bridge += truck_weights[i]
            i+=1
        else:
            G.crossing.put(0)
        G.time += 1

    return G.time


# 풀고 나서 후기 -> 코드를 작성하면서도 무게 0 짜리 가짜 트럭을 집어 넣는 방법이 끔찍하다 생각했건만
# 다른 사람들도 가짜 트럭을 사용하는 걸 보았다... 이보다 더 나은 방법은 없는 걸까?


def solution2(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    sec = 0
    while q:
        sec += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights._pop(0))
            else:
                q.append(0)
    return sec


# 또 다른 풀이

import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution3(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count



