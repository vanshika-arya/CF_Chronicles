n=int(input())
for i in range (1,n+1):
    a,b,c,d=map(int,input().split())
    if(a==b==c==d):
        print("YES")
    else:
        print("NO")