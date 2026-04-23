n, m, k = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

row = list(range(n))
col = list(range(m))

for _ in range(k):
    s = input().split()
    
    if s[0] == 'r':
        x, y = int(s[1])-1, int(s[2])-1
        row[x], row[y] = row[y], row[x]
        
    elif s[0] == 'c':
        x, y = int(s[1])-1, int(s[2])-1
        col[x], col[y] = col[y], col[x]
        
    else:            
        x, y = int(s[1])-1, int(s[2])-1
        print(a[row[x]][col[y]])