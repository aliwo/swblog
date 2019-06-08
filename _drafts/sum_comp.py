import dis
import time
import sys
from datetime import datetime

sys.setrecursionlimit(20000)

def recursive_sum(n):
    if n == 1:
        return 1
    return n + recursive_sum(n-1)


def fast_sum(n):
    if n == 1:
        return 1
    if n % 2 == 1:
        return fast_sum(n-1) + n
    return 2*fast_sum(n//2) + (n//2) ** n



print(datetime.now())
fast_sum(3900)
print(datetime.now())

print('\n\n\n')

print(datetime.now())
recursive_sum(3900)
print(datetime.now())


