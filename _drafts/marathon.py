import datetime

weekdays = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}

def solution(a, b):
    return weekdays[datetime.datetime(2016, a, b).weekday()]


