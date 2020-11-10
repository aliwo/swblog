# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
class ContinuousMedianHandler:

    def __init__(self):

        # 혹은 pointer 는 하나만 쓰고, 짝수 일 때는 pointer - 1 의 숫자를 같이 사용하는 방법도 있다.

        # pointer 왼쪽에 수를 추가하는 경우 (포인터가 가리키는 값보다 작은 경우)
        #   - 추가해서 짝수가 되는 경우 [3, 4*, 5] -> [2, 3, 4*, 5] -> pointer 1 증가
        #   - 추가해서 홀수가 되는 경우 [4, 5*] -> [3, 4*, 5] -> pointer 그대로

        # pointer 오른쪽에 수를 추가하는 경우 (포인터가 가리키는 값보다 큰 경우)
        #   - 추가해서 짝수가 되는 경우 [3, 4*, 5] -> [3, 4, 5*, 6] -> pointer 1 증가
        #   - 추가해서 홀수가 되는 경우 [4, 5*] -> [4, 5*, 6] -> pointer 그대로

        # pointer 와 같은 값을 추가하는 경우도
        #   - 짝수는 pointer 1 증가
        #   - 홀수는 그대로
        self.median = None
        self.numbers = []
        self.is_odd = False
        self.pointer = 0

    def insert(self, number):
        # Write your code here.
        for i in range(len(self.numbers)):
            if self.numbers[i] >= number:
                self.numbers.insert(i, number)
                break
        else:
            self.numbers.append(number)

        if self.is_odd == True:
            self.pointer += 1
        self.is_odd = not self.is_odd

        if not self.is_odd:
            self.median = (self.numbers[self.pointer] + self.numbers[self.pointer - 1]) / 2
        else:
            self.median = self.numbers[self.pointer]


    def getMedian(self):
        return self.median

cmh = ContinuousMedianHandler()
cmh.insert(5)
cmh.insert(10)
print(cmh.getMedian()) # 7.5
cmh.insert(20)
cmh.insert(12)
cmh.insert(10)
print(cmh.getMedian())



