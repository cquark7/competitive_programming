from sys import stdin, stdout


def f(n):
    n = int(n)
    ans = 0
    while n > 1:
        a = n // 5
        ans += a
        n = a
    return str(ans)


print('\n'.join(map(f, (stdin.readline() for t in range(int(input()))))))
