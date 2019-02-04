# vending_machine.py
# 자판기의 음료수 목록
merchandise = ['파워에이드', '코카콜라', '칠성사이다', '게토레이', '포카리스웨트', '스프라이트', '핫식스']

# 마시고 싶은 음료수를 선택하자.
number = int(input()) # 사용자는 0과 6사이에서 선택하면 된다.

print(merchandise[number])
print('를 자판기에서 뽑았다!')