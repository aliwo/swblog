import threading
# programmer 쓰레드 사용가능 여부 테스트... 되는데? 런타임 에러는 보이지 않는다.

def say_hi():
    print('hi')


my_thread = threading.Thread(target=say_hi)
my_thread.run()


