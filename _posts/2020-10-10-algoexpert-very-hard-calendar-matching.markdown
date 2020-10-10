---
layout: single
title:  "갓갓 익스퍼트: calendar matching"
date:   2020-10-10 11:10:03 +0900
categories: [algorithm]
--- 

## 문제
algo expert의 calendar matching 을 풀어 보았습니다.
문제 본문은 저작권이 있기 때문에 한글로 간략하게 설명만 적곘습니다. 두 직원이 저마다의 
스케쥴을 갖고 있습니다. 두 직원이 "모두" 스케쥴이 비어있는 때에 회의를 잡고 싶습니다.
- 직원1의 스케쥴이 리스트에 주어집니다. `calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]`
- 직원1의 출근시간과 퇴근시간이 주어집니다. `dailyBounds1 = ["9:00", "20:00"]`
- 직원2의 스케쥴이 리스트에 주어집니다. `calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]`
- 직원2의 출근시간과 퇴근시간이 주어집니다. `dailyBounds2 = ["10:00", "18:30"]`
- 회의시간의 길이가 주어집니다. (분 단위) `meetingDuration = 30`

회의가 가능한 모든 시간을 리턴해야 합니다.
- `[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]`
- 결과값은 오름차순으로 정렬되어야 합니다.

주의: 
- `calendar1`, `calendar2` 는 오름차순 정렬된 상태로 주어집니다.
- 시간은 `military time` 형식으로 주어집니다. `8:30`, `9:01`, `23:56` 

## 문제에 접근하기
저는 시간을 주제로 한 문제를 만나면
어짜피 하루는 24시간이고 1시간은 60분... 이렇게 범위가 정해져 있다는 특성을 적극 활용합니다.

1시간이 60분, 하루가 24시간이니까 하루는 총 1440분입니다. 이 문제에서 '초' 까지는 고려하지 않으니
하루를 1440분으로 정해 놓으면 딱이죠.

- 길이 1440 짜리 True 로만 이루어진 리스트 `ca`(calendar array)를 미리 만들어 놓은 후,
- calendar1 을 회전하면서 직원1이 회의할 수 없는 시간을 모두 False 로 세팅
- 출근시간 전과 퇴근시간 후도 모두 False 로 
- 직원 2도 똑같이 합니다.
- 마지막으로 ca 를 한 번 회전합니다. 
- 위 과정을 거친 후에도 배열에서 여전히 True 로 남아있는 부분이 바로 "회의할 수 있는 시간" 입니다.
- 회의할 수 있는 시간을 모두 기록한 후 리턴하면 됩니다.

쉽죠? 솔직히 hard 에 이것보다 어려운 문제들이 엄청 많은데 왜 이게 very hard 인지 모르겠습니다.


## time 을 index 로, 다시 index 를 time 으로
이 문제를 위와 같은 접근법으로 푼다고 했을 때, 아마도 (그나마) 어려운 부분은 
어떻게 시간 문자열을 -> 배열 인덱스로 바꾸는가, 그리고 배열 인덱스를 다시 시간으로 바꾸는 가
일겁니다.

```python
def index2time(index):
    '''
    60 으로 나눈 나머지와 몫을 구한다.
    '''
    hour = index // 60
    minute = index % 60
    return f'{hour}:{str(minute).zfill(2)}'


def time2index(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)
```

인데스를 시간으로 바꾸려면 인덱스를 60 으로 나눈 나머지와, 몫이 모두 필요합니다.
나머지와 몫을 구했다면 f-스트링과 zfill 을 사용해서 적당히 `military format` 으로 바꿔준 후 리턴합니다.

시간을 인덱스로 바꾸는 건 더 간단합니다. : 를 기준으로 split() 한 뒤에, 시간에 해당하는 부분에만 60을 곱해주면 되죠.
`시간 * 60`과 `분`을 합산해서 리턴합니다.


## 전체 코드
```python
def index2time(index):
    '''
    60 으로 나눈 나머지와 몫을 구한다.
    '''
    hour = index // 60
    minute = index % 60
    return f'{hour}:{str(minute).zfill(2)}'


def time2index(time):
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    result = []
    ca = [True for _ in range(1440)]

    # calendar1 & dailyBound1 에 대한 처리
    for elem in calendar1:
        for i in range(time2index(elem[0]), time2index(elem[1])):
            ca[i] = False
    for i in range(0, time2index(dailyBounds1[0])):
        ca[i] = False
    for i in range(time2index(dailyBounds1[1]), len(ca)):
        ca[i] = False

    # calendar2 & dailyBound2 에 대한 처리
    for elem in calendar2:
        for i in range(time2index(elem[0]), time2index(elem[1])):
            ca[i] = False
    for i in range(0, time2index(dailyBounds2[0])):
        ca[i] = False
    for i in range(time2index(dailyBounds2[1]), len(ca)):
        ca[i] = False

    i = 0
    while i < len(ca):
        if ca[i] == True:
            start = i
            while ca[i] == True:
                i += 1
            end = i
            if end - start >= meetingDuration:
                result.append([index2time(start), index2time(end)])
        i += 1
    return result
```

마지막에 ca 를 회전하는 부분을 부가 설명하자면...
- `ca[i] == True` 를 만나면 기록을 시작합니다. 시작지점을 기록합니다. `start = i`
- 내부 while 문을 써서 더 이상 ca[i] 가 True 가 아닐 때 까지 i 를 증가시킵니다.
- while 문을 빠져나왔다는 것은 종료지점에 다다랐다는 것입니다. end 를 기록합니다. `end = i`
- `end - start` 를 해 봅니다. 회의 시간보다 값이 큰가요? 그러면 그 시간동안 회의를 할 수 있는 겁니다.
- 따라서 `[start, end]` 를 결과 result 에 append() 합니다. 단, index 가 아니라 military time 으로 바꿔줘야 겠죠