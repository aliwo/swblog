def sub(a, b):
    if a > b:
        return a - b
    return b - a

def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    result = 999999
    for x in arrayOne:
        for y in arrayTwo:
            cur = sub(x, y)
            if cur < result:
                result = cur
            else:
                break
    return result

print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))