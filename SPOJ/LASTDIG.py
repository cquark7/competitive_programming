from sys import stdin

input = stdin.readline
d2 = {n: {p % 4: str(n ** p)[-1] for p in range(4, 8)} for n in range(10)}
for tc in range(int(input())):
    a, b = input().split()
    print(d2[int(a[-1])][int(b[-2:]) % 4] if b != '0' else '1')
