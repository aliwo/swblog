# def solution(number, k):
#     temp = []
#     for i, num in enumerate(number):
#         temp.append((num, i))
#     temp.sort()
#     temp = temp[k:]
#
#     temp.sort(key=lambda elem: elem[1])
#
#     return ''.join([elem[0] for elem in temp])


def solution(number, k):
    for _ in range(k):
        for i in range(len(number)-1):
            if int(number[i]) < int(number[i+1]):
                number = number[:i] + number[i+1:]
                break
    return number

print(solution("1924", 2))
print(solution("4177252841", 4))