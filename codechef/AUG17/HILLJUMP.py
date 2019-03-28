import numpy
from sys import stdin, stdout

input = stdin.readline

n, q = map(int, input().split())

h = numpy.r_[0, list(map(int, input().split()))]

for x in range(q):
    a = input()
    if a[0] == '1':
        typ, i, k = map(int, a.split())
        cnt, maxjumps, currentHill, j = 0, 100, i, i + 1
        while cnt < k and maxjumps and j <= n:
            if h[j] > h[currentHill]:
                cnt += 1
                maxjumps = 100
                currentHill = j
            else:
                maxjumps -= 1
            j += 1
        stdout.write("%d\n" % currentHill)
    else:
        typ, L, R, X = map(int, a.split())
        h[L:R + 1] += X
