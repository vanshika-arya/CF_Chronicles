n, x = map(int, input().split())
distress = 0
for _ in range(n):
    op, d = input().split()
    d = int(d)
    
    if op == '+':
        x += d
    else:
        if x >= d:
            x -= d
        else:
            distress += 1
print(x, distress)