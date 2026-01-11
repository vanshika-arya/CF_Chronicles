n,a,b=map(int, input().split())
sum=0
for i in range(1,n+1):
    original = i
    s=0
    while i>0:
        digit=i%10
        s=s+digit
        i=i//10
    if a<=s <=b:
        sum+=original
print(sum)