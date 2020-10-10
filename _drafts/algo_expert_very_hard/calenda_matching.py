

strategy = '''
하루를 1440 분으로 환산. 길이 1440 의 True 배열을 1개 만든다.
ca = [True for _ in range(1440)] # calendar array
ca 에 calendar 1 에 해당하는 부분을 전부 False 로 치환
ca 에 calendar 2 에 해당하는 부분을 전부 False 로 치환

i = 0
while i < len(ca):
    if ca[i] == True:
        # 시작 지점 기록
        while ca[i] == True:
            i += 1
        # 종료 지점 기록
        # if meetingDuration 보다 길다면:
        #   답에 append
    c1 += 1
    c2 += 1
'''

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
            # 만약 맨 끝에 도달한다면?
        i += 1
    return result

print(calendarMatching(
[["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]],
["9:00", "20:00"],
[["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]],
["10:00", "18:30"],
30
))


