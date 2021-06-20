from functools import wraps
from time import sleep, time


class TimedValue:

    def __init__(self, value, time=time()):
        self.value = value
        self.time = time

    def bind(self, f):
        '''
        f() 는 TimedValue 객체를 반환하는 함수.
        '''
        timed_value = f(self.value)
        new_value = timed_value.value
        new_time = self.time + timed_value.time
        return TimedValue(new_value, new_time)


def time_it(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        return TimedValue(result, end - start)
    return wrapper


@time_it
def fast(x):
    return x + 1


@time_it
def slow(x):
    sleep(0.1)
    return x + 1


@time_it
def slow2(x):
    sleep(0.1)
    return x + 2


timed_value = fast(1).bind(slow).bind(slow2)


value = timed_value.value
time_spent = timed_value.time

print(value, time_spent)
