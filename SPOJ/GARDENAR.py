from sys import stdin, stdout

ans = ''
for t in range(int(input())):
    d, e, f = map(int, stdin.readline().split())
    s = (d + e + f) / 2
    area = 0.2165063509 * (d ** 2 + e ** 2 + f ** 2) + 1.5 * (s * (s - d) * (s - e) * (s - f)) ** 0.5
    stdout.write("%.2f\n" % area)
