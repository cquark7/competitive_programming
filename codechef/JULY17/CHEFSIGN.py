for t in range(int(input())):
    s = input()
    ans = count = 0
    last = s[0]
    for c in s:
        if c == '=':
            continue
        if c == last:
            count += 1
        else:
            ans = max(ans, count)
            count = 1
            last = c
    print(max(ans, count)+1)
