import sys


def dp1(n):
    if n < 12:
        return n
    if n in d:
        return d[n]
    ans = dp1(n // 2) + dp1(n // 3) + dp1(n // 4)
    d[n] = ans
    return ans


for x in sys.stdin:
    d = {}
    print(dp1(int(x)))
