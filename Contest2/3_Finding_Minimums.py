n,k = map(int, input().split())
a=list(map(int, input().split()))
i=0
res=[]
while i<n:
    m=a[i]
    j=i
    while j<n and j<i+k:
        if a[j]<m:
            m=a[j]
        j+=1
    res.append(m)
    i=i+k
print(*res)
