
strategy = '''
강의 들음.

precomputation 을 사용해서 시간복잡도를 줄이는 게 핵심.

인덱스를 리턴
'''

def apartmentHunting(blocks, reqs):
    memo = {req: [float('inf') for _ in range(len(blocks))] for req in reqs}

    for req in reqs:
        memo[req][0] = 0 if blocks[0][req] == True else memo[req][0]
        for i in range(1, len(blocks)):
            memo[req][i] = 0 if blocks[i][req] == True else memo[req][i-1] + 1
        for i in reversed(range(len(blocks)-1)):
            memo[req][i] = 0 if blocks[i][req] == True else min(memo[req][i+1] + 1, memo[req][i])

    temp = []
    for i in range(len(blocks)):
        max_value = 0
        for req in reqs:
            max_value = max(memo[req][i], max_value)
        temp.append((max_value, i))
    temp.sort()

    return temp[0][1]


# print(apartmentHunting([
#   {"gym": False, "school": True, "store": False},
#   {"gym": True, "school": False, "store": False},
#   {"gym": True, "school": True, "store": False},
#   {"gym": False, "school": True, "store": False},
#   {"gym": False, "school": True, "store": True}
# ], ["gym", "school", "store"]))

print(apartmentHunting([
  {"gym": False, "office": True, "school": True, "store": False},
  {"gym": True, "office": False, "school": False, "store": False},
  {"gym": True, "office": False, "school": True, "store": False},
  {"gym": False, "office": False, "school": True, "store": False},
  {"gym": False, "office": False, "school": True, "store": True}
], ["gym", "office", "school", "store"]))