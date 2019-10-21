import heapq

def solution(lists):
    merged_list = []

    # 모든 리스트의 0번째 요소가 들어있는 heap 을 init
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        # heap 에서 하나를 꺼내 결과 리스트에 append() 한다.
        val, list_ind, element_ind = heapq.heappop(heap)
        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]): # IndexError 를 막기 위함.
            # 힙에 다음 요소를 추가한다.
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list

print(solution([[1,2,4], [2,3,4], [1,3,5]]))

