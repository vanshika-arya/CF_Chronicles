t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    i = 1
    
    while i + 5 <= n:
        res += [i, i+2, i+3, i+1, i+4, i+5]
        i += 6
    
    rem = n - i + 1
    
    if rem == 1:
        res += [i]
    elif rem == 2:
        res += [i, i+1]
    elif rem == 3:
        res += [i, i+2, i+1]
    elif rem == 4:
        res += [i, i+2, i+3, i+1]
    elif rem == 5:
        res += [i, i+2, i+3, i+1, i+4]
    
    print(*res)