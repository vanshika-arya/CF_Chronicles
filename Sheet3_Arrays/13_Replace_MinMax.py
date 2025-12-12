n=int(input())
a=list(map(int,input().split()))
min=a[0]
max=a[0]
b=[]
for i in a:
    if i<min:
        min=i
    if i>max:
        max=i
for j in a:
    if j==min:
        j=max
        b.append(j)
    elif j==max:
        j=min
        b.append(j)
    else:
        b.append(j)
print(*b)