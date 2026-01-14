n=int(input())
# for i in range(n):
#     if 2**i==n:
#         print("YES")
#         break
# else:
#     print("NO")
i=1
while i<n:
    i=i*2
if i==n:
    print("YES")
else:
    print("NO")