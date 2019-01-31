import numpy
from sys import stdout


def sieve8(n):
    prime = numpy.ones(n // 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(3, int(n ** .5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[p * p // 3::2 * p] = False
            prime[p * (p - 2 * (i & 1) + 4) // 3::2 * p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    for p in range(99, 5761400, 100):
        stdout.write("%d\n" % result[p])
    return 0


# return numpy.r_[2, result]

stdout.write('2\n')
b = sieve8(99998954)
