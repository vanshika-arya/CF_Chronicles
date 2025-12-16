n, m = map(int, input().split())
a= [input() for k in range(n)]
x,y = map(int, input().split())
x-=1
y-=1
for i in [-1, 0, 1]:
    for j in [-1,0,1]:
        if i==0 and j==0:
            continue
        ni,nj = x + i, y + j
        if 0 <= ni < n and 0 <= nj < m:
            if a[ni][nj] != 'x':
                print("no")
                exit()
print("yes")
