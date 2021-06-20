from copy import deepcopy


class Num:
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return str(self.num)

a = [1, 2, 3]
b = [Num(1), Num(2), Num(3)]

# 할당

a1 = a
b1 = b
print('할당')
a1.append(4)
print(a)
b1.append(Num(4))
print(b)
print()

# 얕은 복사
print('얕은 복사')
a2 = a[:]
b2 = b[:]

a2.append(5)
print(a)
print(a2)
b2.append(Num(5))
print(b)
print(b2)

print('얕은 복사와 mutable')
b2[0].num = 999
print(b)
print(b2)
print()


# 깊은 복사
print('깊은 복사')
b3 = deepcopy(b)
b3[0].num = 1
print(b)
print(b3)







