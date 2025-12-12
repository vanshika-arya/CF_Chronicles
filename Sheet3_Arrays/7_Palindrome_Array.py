n=int(input())
a=list(map(int,input().split()))
l=a[::-1]
if a==l:
    print("YES")
else:
    print("NO")