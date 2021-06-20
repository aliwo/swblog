import heapq


heap = [-3, -5, -2, -1, -7, -8, -4]
heapq.heapify(heap)

heap.append(-6)
heap.append(-9)

print(heap)

# Arr[(i -1) / 2] returns its parent node.
# Arr[(2 * i) + 1] returns its left child node.
# Arr[(2 * i) + 2] returns its right child node.
# [-8, -7, -4, -1, -5, -2, -3, -6, -9]
# 7 index = 1 -> 왼쪽 자식은 arr[3] 1 오른쪽 자식은 arr[4] 5
# 4 index = 2 -> 왼쪽 자식은 arr[5] 2 오른쪽 자식은 arr[6] 3