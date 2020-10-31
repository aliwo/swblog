from collections import deque
# ord('z') = 122

def ord2(char):
    return ord(char) - 96


# def rotate(word, num):
#     '''
#     양수면 왼쪽으로 rotate
#     음수면 오른쪽으로 rotate
#     '''
#     if len(word) <= 1:
#         return word
#
#     if num == 0:
#         pass
#     elif num > 0: # 양수면
#         for _ in range(abs(num)):
#             word.append(word.popleft())
#     else:
#         for _ in range(abs(num)): # 음수면
#             word.appendleft(word.pop())
#     return word




def solution(encrypted_text, key, rotation):
    temp = deque([ord(char) for char in encrypted_text])
    temp_key = deque([ord(char) for char in key])

    temp.rotate(-rotation)

    for i in range(len(temp_key)):
        temp[i] = temp[i] - temp_key[i] + 96
        if temp[i] < 97:
            temp[i] = 123 - (97 - temp[i])

    return ''.join([chr(elem) for elem in temp])


print(solution('qyyigoptvfb', 'abcdefghijk', 3))