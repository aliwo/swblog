

class Palindrome:
    def __init__(self, word):
        self.word = word
        self.length = len(word)

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __eq__(self, other):
        return self.length == other.length

    def __repr__(self):
        return self.word


def max_even_palindrome_length(string, i):
    '''
    가운데 지점
    (i-2),(i-1)|i,(i+1)
    '''
    j = i - 1
    while j > 0 and i < len(string) and string[j] == string[i]:
        j -= 1
        i += 1
    return Palindrome(string[j:i+1])


def max_odd_palindrome_length(string, i):
    j = i - 1
    i += 1
    while j > 0 and i < len(string):
        if string[j] != string[i]:
            return Palindrome(string[j+1:i])
        j -= 1
        i += 1
    return Palindrome(string[j:i+1])


def longestPalindromicSubstring(string):
    # Write your code here.
    max_palindrome = Palindrome('')

    if len(string) <= 1:
        return string

    for i in range(1, len(string)):
        max_odd = max_odd_palindrome_length(string, i)
        max_even = max_even_palindrome_length(string, i)
        max_palindrome = max(max_odd, max_even, max_palindrome)
    return max_palindrome.word


# print(max_odd_palindrome_length('abcba', 2).word)
# print(max_odd_palindrome_length('axyzzyxx', 1).word)
# print(longestPalindromicSubstring('abaxyzzyxxf'))
print(longestPalindromicSubstring('ab12365456321bb'))


