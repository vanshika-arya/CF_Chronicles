n,m =map(int,input().split())
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    b.extend(a)
    # if len(a)>=2:
    #     b=a[0]
    #     c=a[1]
    #     d.append(b)
    #     d.append(c)
x=int(input())
if x in b:
    print("will not take number")
else:
    print("will take number")