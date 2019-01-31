n = int(input())
if n == 0:
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    ans = 0
    while n % 2 == 0:
        ans += 1
        n //= 2
    print(ans * 2)
