sort = {
    'rock': 0,
    'pop': 1,
    'classic': 2
}


my_list = [(1000, 'classic'), (200, 'pop'), (300, 'rock')]
# 기본 정렬. 튜플의 0번 요소를 기준으로 오름차순 정렬된다.
print(sorted(my_list)) # pop -> rock -> classic
# 딕셔너리 sort 를 사용한 정렬
print(sorted(my_list, key=lambda x: sort[x[1]])) # rock -> pop -> classic



