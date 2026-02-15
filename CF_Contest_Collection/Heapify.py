t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    temp = True
    while temp:
        temp = False
        for i in range(n//2):
            if a[i] > a[2*i+1]: 
                a[i], a[2*i+1] = a[2*i+1], a[i]
                temp = True
    if a == sorted(a):
        print("YES")
    else:
        print("NO")
