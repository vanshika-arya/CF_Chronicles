t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if 67 in a:
        print("YES")
        continue
    for j in range(n):
        for k in range(j+1,n):
            if a[j]*a[k]==67:
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")    
    