from bisect import bisect_right as BR, bisect_left as BL
from itertools import compress

bound = 46340


def half_sieve(n):
    sieve = bytearray([True]) * (n >> 1)
    false = bytearray([False])
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i >> 1]:
            sieve[i * i >> 1::i] = false * ((n - i * i - 1) // (2 * i) + 1)
    primes = list(compress(range(1, n, 2), sieve));
    primes[0] = 2
    return primes


primes = half_sieve(bound)


def segmented_sieve(m, n):
    limit = int(n ** 0.5)
    sieve = bytearray([True]) * ((n - m >> 1) + 1)
    false = bytearray([False])
    r = BR(primes, limit)
    for p in primes[1:r]:
        fm = (abs(-m // p) | 1) * p
        sieve[fm - m >> 1::p] = false * ((n - fm) // (2 * p) + 1)
    print('\n'.join(map(str, compress(range(m, n + 1, 2), sieve))))


for tc in range((int(input()))):
    m, n = map(int, input().split())
    if m < bound:
        print('\n'.join(map(str, primes[BL(primes, m): BL(primes, n + 1)])))
        if n < bound: continue
        m = bound
    segmented_sieve(m | 1, n)
