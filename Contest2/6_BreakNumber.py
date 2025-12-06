n=int(input())
max_count=0
a=list(map(int,input().split()))
for i in a:
    count = 0
    while i%2==0:
        count+=1
        i=i//2
    if max_count<=count:
        max_count=count
print(max_count)