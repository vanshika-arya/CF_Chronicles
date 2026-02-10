n,k=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(n):
    if l[i]>=l[k] and l[i]>0:
        count+=1
print(count)