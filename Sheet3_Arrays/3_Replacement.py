n=int(input())
a=list(map(int,input().split()))
p=[]
for i in a:
    if i<0:
        i=2
        p.append(i)
    elif i==0:
        p.append(i)
    else:
        i=1
        p.append(i)
print(*p)
        