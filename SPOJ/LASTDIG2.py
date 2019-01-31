d2 = {n: {p % 4: str(n ** p)[-1] for p in range(4, 8)} for n in range(10)}
for tc in range(int(input())):
    a, b = input().split()
    b = int(b)
    print(d2[int(a[-1])][b % 4] if b else '1')
