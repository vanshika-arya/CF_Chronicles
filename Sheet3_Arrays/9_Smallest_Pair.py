t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res=a[0]+a[1]+2-1
    for j in range(n):
        for k in range(j+1, n):
            s = a[j]+a[k]+(k+1)-(j+1)
            if s<res:
                res=s
    print(res)

