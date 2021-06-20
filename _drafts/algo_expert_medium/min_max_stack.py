# Feel free to add new properties and methods to the class.
import heapq

class MinMaxStack:
    '''
    매번 push 할 때 마다 min 과 max 의 snapshot 을 찍는다.
    pop() 할 때 마다 snapshot 을 날려버린다. (min max 를 수행하는 데에는 heap 보다도 더 효율적이다.)
    '''
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        pass

    def push(self, number):
        # Write your code here.
        pass

    def getMin(self):
        # Write your code here.
        pass

    def getMax(self):
        # Write your code here.
        pass
