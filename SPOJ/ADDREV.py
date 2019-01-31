from sys import stdin, stdout

results = ''
for t in range(int(input())):
    m, n = stdin.readline().split()
    results += str(int(m[::-1]) + int(n[::-1]))[::-1].lstrip('0') + '\n'
stdout.write(results)
