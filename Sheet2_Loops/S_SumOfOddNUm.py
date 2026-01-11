t=int(input())
for i in range(1,t+1):
    x,y=map(int, input().split())
    sum=0
    for j in range(min(x,y)+1,max(x,y)):
        if j%2!=0:
            sum+=j
    print(sum)