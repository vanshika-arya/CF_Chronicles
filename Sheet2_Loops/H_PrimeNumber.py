n=int(input())
if n==1:
    print("NO")
else:
    i=2
    while i*i<=n:
        if n%i==0:
            print("NO")
            break
        i+=1
    else:
        print("YES")
