n, h=map(int,input().split())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    if l[i]>h:
        sum+=2
    else:
        sum+=1
print(sum)