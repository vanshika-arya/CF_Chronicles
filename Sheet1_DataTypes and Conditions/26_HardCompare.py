import math
a,b,c,d=map(int,input().split())
left= b*math.log(a)
right= d*math.log(c)

if(left>right):
    print("YES")
else:
    print("NO")

