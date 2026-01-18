# n=int(input())
# s=0
# count=0
# i=1
# while s+i<=n:
#     s+=i
#     count+=1
#     i+=1
# print(count)
n = int(input())
k = int((2*n)**0.5)
if k*(k+1)//2 > n:
    k -= 1
print(k)
