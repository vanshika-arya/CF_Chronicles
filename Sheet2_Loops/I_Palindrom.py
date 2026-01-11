n=int(input())
ori_n=n
res=0
while n>0:
    digit=n%10
    res=res*10+digit
    if res==0:
        n=n//10
    else:
        n=n//10  
print(res)
if ori_n==res:
    print("YES")
else:
    print("NO")

