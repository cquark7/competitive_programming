from sys import stdin

s = {'714', '1120149658760', '74049690', '2', '15', '23843770274', '796030994547383610', '4895', '7677619978602',
     '16944503814015855', '163427632719', '10803704', '3478759200', '0', '229970', '104', '2472169789339634', '33552',
     '116139356908771352', '1576239', '507544127', '52623190191455', '360684711361584'}

t = int(input())
out = ['0'] * t
for i in range(t):
    n = stdin.readline().rstrip()
    if n in s:
        out[i] = '1'
print('\n'.join(out))
