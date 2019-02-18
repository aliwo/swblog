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