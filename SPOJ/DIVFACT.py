from sys import stdin, stdout

M = 10 ** 9 + 7


def prime_sieve(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


primes = prime_sieve(50000)


def facDivCnt(n):
    cnt = 1
    for p in primes:
        tmp = n // p
        if not tmp:
            break
        exp = 0
        p_power = p
        while tmp:
            exp += tmp
            p_power *= p
            tmp = n // p_power
        if exp:
            cnt = (cnt * (exp + 1)) % M
    return cnt


nums = map(int, (stdin.readline() for x in range(int(stdin.readline()))))
for n in nums:
    stdout.write("%d\n" % facDivCnt(n))
