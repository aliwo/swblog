def my_func(a, b, c):
    pass

def my_func2(a=1, b=2, c=3):
    pass

def my_func3(a, b=2):
    pass

def my_func4(a=1, b): # 에러!!
    pass



class DolceLatte:

    def __init__(self, shot, syrup, milk, ice, whip, *args):
        self.shot = shot # 1 ~ 5 숫자
        self.syrup = syrup # 1 ~ 5 숫자
        self.milk = milk # '일반', '저지방', '무지방', '두유'
        self.ice = ice # True 혹은 False
        self.whip = whip # True 혹은 False

        print(type(args))
        self.almond = args.count('아몬드')
        self.cashnut = args.count('캐슈넛')
        self.walnut = args.count('호두')


nut_dolce_latte = DolceLatte(4, 1, '저지방', False, False, '아몬드', '아몬드', '호두')


























