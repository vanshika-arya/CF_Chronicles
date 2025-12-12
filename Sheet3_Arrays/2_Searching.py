n=int(input())
a=list(map(int,input().split()))
x=int(input())
if x in a:
    print(a.index(x))
else:
    print("-1")