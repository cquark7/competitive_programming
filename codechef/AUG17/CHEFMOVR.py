for tc in range(int(input())):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    ans, summ = -1, sum(arr)
    if summ % n == 0:
        flag, mean = True, summ//n
        arr = list(map((-mean) .__add__, arr))
        for i in range(d):
            if sum(arr[i::d]): flag = False;break
            for j in range(i+d, n, d): arr[j] += arr[j-d]
        if flag: ans = sum(map(abs, arr))
    print(ans)
