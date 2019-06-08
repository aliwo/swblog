import time
from _drafts.BRIDGE_CROSS import solution as sw
from _drafts.BRIDGE_CROSS import solution2 as s2
from _drafts.BRIDGE_CROSS import solution3 as s3

BRIDGE_LENGTH = 1500
BRIDGE_WEIGHT = 10000
TRUCK = [900] * 9999

# 내가 더 빠르다 ^^ 내 꺼 11초 남의꺼 31초
print(time.strftime('%X'))
print(sw(BRIDGE_LENGTH, BRIDGE_WEIGHT, TRUCK))
print(time.strftime('%X'))

print('-----------------------------------------')

print(time.strftime('%X'))
print(s3(BRIDGE_LENGTH, BRIDGE_WEIGHT, TRUCK))
print(time.strftime('%X'))

