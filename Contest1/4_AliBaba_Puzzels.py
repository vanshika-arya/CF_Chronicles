a,b,c,d=map(int,input().split())
list=[]
# list.append(a+b+c)
list.append(a+b-c)
list.append(a+b*c)
list.append(a-b+c)
list.append(a*b+c)
list.append(a*b-c)
list.append(a-b*c)
# list.append(a*b*c)
# list.append(a-b-c)

if list.__contains__(d):
    print("YES")
else:
    print("NO")
