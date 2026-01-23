# a,b,x=map(int,input().split())
# sum=0
# for i in range(a,b+1):
#     if i%x==0:
#         sum+=i
# print(sum)

a,b,x = map(int, input().split())
if a>b:
    a,b = b,a
first = ((a + x - 1) // x) * x   
last = (b // x) * x             
if first > last:
    print(0)
else:
    n = ((last - first)//x)+1
    print(n*(first + last)//2)
