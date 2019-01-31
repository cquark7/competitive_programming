from sys import stdout, stdin

m = 1000000007
dic = {0: (0, 1)}


def fib(n):
    if n in dic:
        return dic[n]
    a, b = fib(n >> 1)
    c = (a * (2 * b - a)) % m
    d = (a * a + b * b) % m
    if n & 1:
        dic[n] = (d, c + d)
        return d, c + d
    dic[n] = (c, d)
    return c, d


t = int(stdin.readline())
for tc in range(t):
    L, R = map(int, stdin.readline().split())
    stdout.write("%d\n" % ((fib(R + 2)[0] - fib(L + 1)[0]) % m))
