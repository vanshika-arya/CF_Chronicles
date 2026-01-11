# k,s=map(int,input().split())
# count=0
# sum=0
# for i in range(0,k+1):
#     for j in range(0,k+1):
#         for m in range(0,k+1):
#             if i+j+m==s:
#                 count+=1 
# print(count)
k,s= map(int, input().split())
count=0
for i in range(k + 1):
    for j in range(k + 1):
        m=s-i-j
        if 0<=m<=k:
            count+=1
print(count)