t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    count=1      
    temp=1    
    for i in range(1, n):
        if a[i]>=a[i-1]:
            temp+=1
        else:
            temp=1
        count+=temp
    print(count)
