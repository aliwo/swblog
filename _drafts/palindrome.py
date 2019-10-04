def solution(s):
    stack = []
    biggest = 0

    i = 0
    while i < len(s) - 1:

        if len(stack) >= 1:
            if stack[-1] == s[i] or stack[-1] == s[i+1]:
                cur = 2 if stack[-1] == s[i] else 3
                j = i + 1 if stack[-1] == s[i] else i + 2
                stack.pop()
                while j < len(s) and stack:
                    if s[j] == stack[-1]:
                        cur += 2
                        stack.pop()
                        j += 1
                    else:
                        stack = []
                if biggest < cur:
                    biggest = cur
                i = j
                continue

        stack.append(s[i])
        i += 1


    return biggest


print(solution("abccba")) # abccba
print(solution("poiabccbls")) # bccb
print(solution("abcdcba")) # abcdcba
print(solution("abbaxyzazyx")) # xyzazyx
