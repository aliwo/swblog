from collections import Counter

def solution(nums):
    counter = Counter(nums)
    return len(nums) // 2 if len(nums) // 2 <= len(counter.keys()) else len(counter.keys())

