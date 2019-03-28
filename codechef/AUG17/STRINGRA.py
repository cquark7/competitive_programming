from collections import defaultdict
from sys import stdin

def stringra(P, n):
    if 0 in P or any(i not in P for i in range(1, n+1)):
        return [-1]
    for i in range(1, len(P)+1): P[i].sort()
    Q = defaultdict(list)
    Q[1].append(0)
    X = [0]*(n+1)
    k = 0
    for i in range(1, len(P)+1):
        if P[i][0] == 0:
            k += 1
            X[i] = k
        else:
            X[i] = X[P[i][0]]
    for i in range(2, len(P)+1):
        for j in range(i-1, -1, -1):
            if X[i] != X[j]:
                Q[i].append(j)
            else:
                Q[i].append(j)
                break
        Q[i].reverse()
    if any(Q[i] != P[i] for i in range(1, n+1)):
        return [-1]
    return X[1:n+1]

for t in range(int(input())):
    n, m = map(int, stdin.readline().split())
    adjList = defaultdict(list)
    for _ in range(m):
        x, y = map(int, stdin.readline().split())
        adjList[y].append(x)
    print(*stringra(adjList, n))
