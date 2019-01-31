from sys import stdin, stdout

input = stdin.readline
M = 10 ** 8 + 7
for t in range(int(input())):
    n = int(input())
    print("Case {}: {}".format(t + 1, (sum(map(int, input().split())) * 2 ** (n - 1)) % M))
