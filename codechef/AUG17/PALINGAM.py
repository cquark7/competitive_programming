from collections import Counter
from sys import stdin
input = stdin.readline
output = ''
for t in range(int(input())):
    a, b = input(), input()
    fa, fb = Counter(a), Counter(b)
    if any(fa[k] > 1 and k not in fb for k in fa):
        output += 'A\n'
        continue
    keys = {k for k in (set(fa) - set(fb)) if fa[k] == 1}
    winner = 'A' if keys else 'B'
    for ka in keys:
        for kb in fb:
            if kb not in keys:
                winner = 'B'
                break
    output += winner + '\n'
print(output)
