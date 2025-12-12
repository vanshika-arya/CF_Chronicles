n=int(input())
a= list(map(int,input().split()))
d=sum(a)
if d<=0:
    print(abs(d))
else:
    print(d)