from random import randrange


def half_sieve(n):  # 2.36 sec for 10^8
    from itertools import compress
    sieve = bytearray([True]) * (n // 2)
    false = bytearray([False])
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = false * ((n - i * i - 1) // (2 * i) + 1)
    prime = list(compress(range(1, n + 1, 2), sieve))
    prime[0] = 2
    return prime


def miller_rabin2(n, k=3):
    sprimes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}
    if n in sprimes:
        return True
    if n == 1 or any(n % p == 0 for p in sprimes):
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s >>= 1
    for test in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


M = 10 ** 9 + 7
primes = half_sieve(10 ** 6)


def prime_factors6(n):
    if miller_rabin2(n):
        return n % M
    sqrtn = n ** 0.5
    if sqrtn.is_integer() and miller_rabin2(int(sqrtn)):
        return (n * int(sqrtn)) % M
    div_cnt = 1
    n2 = n
    for p in primes:
        if not n % p:
            p_pow = 1
            n //= p
            while not n % p:
                n //= p
                p_pow += 1
            div_cnt *= (p_pow + 1)
        if p * p > n:
            break
    if miller_rabin2(n):
        div_cnt *= 2
    elif (n ** 0.5).is_integer() and n != 1:
        div_cnt *= 3
    elif n != 1:
        div_cnt *= 4
    if div_cnt % 2 == 0:
        return pow(n2, div_cnt // 2, M)
    return (pow(n2, div_cnt // 2, M) * int(n2 ** 0.5)) % M


for t in range(int(input())):
    print(prime_factors6(int(input())))
