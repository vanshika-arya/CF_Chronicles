n,m=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(n):
 s+=a[i]
 a[i]=s
for j in range(m):
 l,r=map(int,input().split())
 print(a[r-1]-(a[l-2] if l>1 else 0))

