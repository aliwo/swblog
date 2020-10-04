strategy = '''
왼쪽 -> 오른쪽으로 이동하면서
+ 만난 첫번째 기둥을 base 로 삼는다.
+ 자기 보다 낮은 기둥이 나타나면 낮은 기둥의 수위를 기록
+ 자기 보다 높은 기둥이 나타나면 자신의 수위를 기록한 뒤, base 기둥을 리셋. 이전까지의 기둥들은 mids 에 추가
이게 맞네
'''

from collections import defaultdict

def waterArea(heights):
    result = 0
    areas = defaultdict(lambda: {'start': 0, 'mids': [], 'end': 0}) # [{'start': 1, 'mids':[4], 'end': 7}]
    area_index = 0

    # 2중 while 써서 i 를 조작해야 할 듯.
    for i in range(len(heights)):
        if heights[i] != 0:
            break

    base = i
    areas[area_index]['start'] = base
    for i in range(i+1, len(heights)):
        if heights[i] == 0:
            continue

        if areas[area_index]['end'] != 0:
            areas[area_index]['mid'].append(areas[area_index]['end'])

        if heights[base] < heights[i]:
            areas[area_index]['end'] = i
            base = i
            area_index += 1
        else:
            areas[area_index]['end'] = i

    print(areas)
    return result


print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))