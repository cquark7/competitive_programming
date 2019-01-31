from collections import Counter
from sys import stdin

for t in range(int(input())):
    acc = [stdin.readline().strip('\n') for x in range(int(input()))]
    d = Counter(acc)
    result = ''
    for i in sorted(d):
        result += i + str(d[i]) + '\n'
    print(result)
    stdin.readline()
