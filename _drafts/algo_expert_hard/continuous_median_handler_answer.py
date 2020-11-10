
# algo expert 의 모범 답안


class ContinuousMedianHandler:
    def __init__(self):
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])
        self.median = None

    def insert(self, number):
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        '''
        큰 쪽에서 작은 쪽으로 몰아줍니다.
        '''
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())

    def updateMedian(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def getMedian(self):
        return self.median


class Heap:
    def __init__(self, comparisonFunc, array):
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

    def buildHeap(self, array):
        pass

    def siftDown(self, currentIdx, endIdx, heap):
        pass

    def siftUp(self, currentIdx, heap):
        pass

    def peek(self):
        pass

    def remove(self):
        pass

    def insert(self):
        pass

    def swap(self):
        pass


def MAX_HEAP_FUNC(a, b):
    return a > b

def MIN_HEAP_FUNC(a, b):
    return a < b