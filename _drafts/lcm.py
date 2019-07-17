def lcm(x, y):
    '''
    최소공배수
    '''
    greater = x if x > y else y

    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

def gcd(x, y):
    '''
    최대 공약수
    '''
    small = y if x > y else x

    for i in range(1, small + 1):
        if ((x % i == 0) and (y % i == 0)):
            gcd = i

    return gcd

def test_lcm():
    assert lcm(3, 9) == 9
    assert gcd(3, 9) == 3


test_lcm()
