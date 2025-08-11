"""
discard all denominations greater than n

"""

def getWays(n, c):
    if n == 0:
        return 1
    else:
        answer = 0
        for coin in c:
            if n - coin < 0:
                continue
            answer += getWays(n - coin, c)
        return answer

print(getWays(5, [1, 4, 5]))
"""
1 1 1 1
1 2 1
1 3
2 2
"""