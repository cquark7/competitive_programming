from collections import defaultdict
import itertools
import os
from sys import stdin, stdout


def iter_sieve(n):  # 2.56 sec for n = 10^8
    izip = itertools.zip_longest
    chain = itertools.chain.from_iterable
    compress = itertools.compress
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    # 2.4x faster than prime_sieve
    zero = bytearray([False])
    size = n // 3 + (n % 6 == 2)
    sieve = bytearray([True]) * size
    sieve[0] = False
    for i in range(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            start = (k * k + 4 * k - 2 * k * (i & 1)) // 3
            sieve[(k * k) // 3::2 * k] = zero * ((size - (k * k) // 3 - 1) // (2 * k) + 1)
            sieve[start::2 * k] = zero * ((size - start - 1) // (2 * k) + 1)
    ans = [2, 3]
    poss = chain(izip(*[range(i, n, 6) for i in (1, 5)]))
    ans.extend(compress(poss, sieve))
    return ans


def prime_factors210(n):
    factors = defaultdict(int)
    for p in primes:
        while n % p == 0:
            factors[p] += 1
            n //= p
        if n == 1:
            break
        if p * p > n > 1:
            factors[n] += 1
            break
    if n < 40052016900:
        return factors
    d = 200130
    p210 = [1, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
            113, 121, 127, 131, 137, 139, 143, 149, 151, 157, 163, 167, 169, 187, 173, 179, 181, 191, 193, 197, 199,
            209]
    while n > 1:
        for p in p210:
            tmp = d + p
            while n % tmp == 0:
                factors[tmp] += 1
                n //= tmp
        d += 210
        if d * d > n > 1:
            factors[n] += 1
            break
    return factors


primes = iter_sieve(200130)

nums = list(map(int, os.read(0, 1000).splitlines()))
i = nums.index(0)
for x in nums[:i]:
    ans = prime_factors210(x)
    output = ''
    for factor in sorted(ans):
        output += '{}^{} '.format(factor, ans[factor])
    print(output.strip())
