import asyncio
import time

async def return_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    return what

async def main():

    task1 = asyncio.create_task(
        return_after(3, 'hello'))

    task2 = asyncio.create_task(
        return_after(1, 'world'))

    print(f"started at {time.strftime('%X')}")

    my_world = await task2
    print(f"line 21 at {time.strftime('%X')}")

    print('do something #2')
    print('do something #3')

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# import asyncio
# import time
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())



# merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']
#
# for drink in merchandise:  # 주의! 복사를 하지 않았을 경우
#     if drink not in ['스프라이트', '핫식스', '코카콜라', '칠성사이다', ]:
#         merchandise.remove(drink)
#
# print(merchandise)

# nums = [1, 2, 3, 4]
# fruit = ["Apples", "Peaches", "Pears", "Bananas"]
# print([(i, f) for i in nums for f in fruit])
# # 출력 결과
# # [(1, 'Apples'), (1, 'Peaches'), (1, 'Pears'), (1, 'Bananas'),
# # (2, 'Apples'), (2, 'Peaches'), (2, 'Pears'), (2, 'Bananas'),
# # (3, 'Apples'), (3, 'Peaches'), (3, 'Pears'), (3, 'Bananas'),
# # (4, 'Apples'), (4, 'Peaches'), (4, 'Pears'), (4, 'Bananas')]
#
#
# result = []
# nums = [1, 2, 3, 4]
# fruit = ["Apples", "Peaches", "Pears", "Bananas"]
#
# for i in nums:
#     for f in fruit:
#         result.append((i, f))
#
#
# print(result)


#
# class DolceLatte:
#
#     def __init__(self, shot, syrup, milk, ice, whip, *args):
#         self.shot = shot # 1 ~ 5 숫자
#         self.syrup = syrup # 1 ~ 5 숫자
#         self.milk = milk # '일반', '저지방', '무지방', '두유'
#         self.ice = ice # True 혹은 False
#         self.whip = whip # True 혹은 False
#
#         print(type(args))
#         self.almond = args.count('아몬드')
#         self.cashnut = args.count('캐슈넛')
#         self.walnut = args.count('호두')
#
#
# nut_dolce_latte = DolceLatte(4, 1, '저지방', False, False, '아몬드', '아몬드', '호두')
#
#
# def swiss_army_knife(target):
#     def knife():
#         print('자릅니다.')
#
#     def nail_clipper():
#         print('손톱을 깎습니다.')
#
#     def opener():
#         print('병을 땁니다.')
#
#     if target == 'knife':
#         return knife
#
#     if target == 'nail_clipper':
#         return nail_clipper
#
#     if target == 'opener':
#         return opener
#
# my_gadget = swiss_army_knife('knife')
# my_gadget() # 자릅니다. 출력
#
# a = 3  # 모듈(파이썬 스크립트 파일) scope
#
#
# def function_1():
#     return a + 1  # 상위 scope 의 a 에 접근한다.
#
#
# function_1()
# print(a)  # a는 모듈 scope 에서 정의되었으므로 함수 호출이 종료되어도 계속 살아남는다.
#
#
#
#
# def my_func(my_list):
#     my_list.append(8)
#
# numbers = [0, 1, 2]
# my_func(numbers)
# print(numbers) # [0, 1, 2, 8]
#
#
#
# class MyClass:
#
#     @classmethod
#     def my_class_method(cls, a):
#         print(a)
#
#     @staticmethod
#     def my_static_method(b):
#         print(b)
#
#
#
