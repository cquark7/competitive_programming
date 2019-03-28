for tc in range(int(input())):
    rArr = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
    n = int(input())
    a = list(map(int, input().split()))
    st = []
    if a[0] == 1:
        st.append(a[0])
    else:
        print('no')
        continue
    for x in a:
        if st[-1] != x:
            st.append(x)
    if st != rArr:
        print('no')
    else:
        if a[:n//2] == a[-1:n//2-(n%2==0):-1] and a[n//2] == 7:
            print('yes')
        else:
            print('no')
