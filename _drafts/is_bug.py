my_list_of_dict = [{}] * 3

my_list_of_dict[0][0] = 1
my_list_of_dict[0][1] = 2

print(my_list_of_dict)
# What I thought : [{0: 1, 1: 2}, {}, {}]
# What actually happened : [{0: 1, 1: 2}, {0: 1, 1: 2}, {0: 1, 1: 2}]

#
# my_list_of_dict = []
#
# for _ in range(3):
#     my_list_of_dict.append({})
#
# my_list_of_dict[0][0] = 1
# my_list_of_dict[0][1] = 2
#
# print(my_list_of_dict) #



