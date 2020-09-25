# 20200825 triumph
# 답지 봤쪙

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
    ways = [0 for _ in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, len(ways)):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]



