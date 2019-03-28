for t in range(int(input())):
    N, Q = map(int, input().split())
    cnt, m1, x = 1, 2**N, 0
    m2 = m1*2-1
    visited = {0}
    for q in range(Q):
        a = list(input().split())
        if a[0] == '?':
            print(cnt)
        else:
            c = int(a[1])
            x = (x % m1 + pow(2, c, m1)) % m1
            arr = bin(x)[-1:1:-1]
            idx = 0
            size = len(arr)-1
            for j in range(N-1, size, -1):
                    idx = idx*2 + 1
                    if idx < m2 and idx not in visited:
                        cnt += 1
                        visited.add(idx)
            for k in range(size, -1, -1):
                if arr[k] == '0':
                    idx = idx * 2 + 1
                    if idx < m2 and idx not in visited:
                        cnt += 1
                        visited.add(idx)
                else:
                    idx = 2 * idx + 2
                    if idx < m2 and idx not in visited:
                        cnt += 1
                        visited.add(idx)
