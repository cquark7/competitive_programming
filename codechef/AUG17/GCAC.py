from sys import stdin, stdout
input = stdin.readline

for tc in range(int(input())):
    a1 = a2 = 0
    N, M = map(int, input().split())
    minSalary = list(map(int, input().split()))
    offeredSalary, maxJobOffers = [0] * M, [0] * M
    for i in range(M):
        offeredSalary[i], maxJobOffers[i] = map(int, input().split())
    qual = [input() for i in range(N)]
    available = maxJobOffers[:]
    for i in range(N):
        maxSalidx = -1
        for j in range(M):
            if qual[i][j] == '1' and available[j] != 0 and minSalary[i] <= offeredSalary[j] and (maxSalidx == -1 or offeredSalary[maxSalidx] < offeredSalary[j]):
                maxSalidx = j
        if maxSalidx != -1:
            a1 += 1
            a2 += offeredSalary[maxSalidx]
            available[maxSalidx] -= 1
    a3 = sum((maxJobOffers[i] == available[i]) for i in range(M))
    stdout.write("%d %d %d\n" % (a1, a2, a3))
