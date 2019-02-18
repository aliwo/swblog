class SpongeBob:
    figure = '네모 모양'
    pants = '네모 바지'
    is_sponge = True

    def cook(self):
        print('버거를 만들어요!')

    def self_introduce(self):
        if self.pants == '네모 바지' and self.is_sponge:
            print('나는 네모 바지 스폰지밥이야!')
        if self.pants != '네모 바지':
            print('내 바지 어디갔어?')


my_sponge_bob = SpongeBob()
my_sponge_bob.self_introduce()

my_sponge_bob.pants = '바지'
my_sponge_bob.self_introduce()




class DolceLatte:

    def __init__(self, shot, syrup, milk, ice, whip):
        self.shot = shot # 1 ~ 5 숫자
        self.syrup = syrup # 1 ~ 5 숫자
        self.milk = milk # '일반', '저지방', '무지방', '두유'
        self.ice = ice # True 혹은 False
        self.whip = whip # True 혹은 False


orders = [(2, 3, '두유', True, True), (4, 1, '저지방', False, False)] # 계속...

lattes = []
for order in orders:
    latte = DolceLatte(*order)
    lattes.append(latte)

print(lattes)













