# # 자판기의 음료수 목록
# merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']
#
# # 마시고 싶은 음료수를 선택하자.
#
# print(merchandise[number])
# print('를 자판기에서 뽑았다!')
#
#
# # number = int(input())


class Noodle:  # 면 클래스 Noodle

    def __init__(self):
        self.ingredients = ['면']  # 모든 면 류 음식의 기본 재료는 '면


class Zza(Noodle):  # 짜장면 클래스 Zza

    def __init__(self):
        Noodle.__init__(self)
        self.ingredients.append('춘장')  # 짜장 = 면 + 춘장


class Zzam(Noodle):  # 짬뽕 클래스 Zzam

    def __init__(self):
        Noodle.__init__(self)
        self.ingredients.append('고추가루')  # 짬뽕 = 면 + 고추가루


class ZzamZza(Zza, Noodle):  # 짬짜면 클래스 Zzam

    def __init__(self):
        Zza.__init__(self)
        Zzam.__init__(self)

my_dinner = ZzamZza()
print(my_dinner.ingredients) # ['면', '고추가루'] 어 춘장 어디갔어


