n = int(input())
a = list(map(int, input().split()))
for i in range(n):           
    if a[i] <= 10:            
        print(f"A[{i}] = {a[i]}")  

# n=int(input())
# a=list(map(int,input().split()))
# for i in range(n):
#     if i<=10 and i in a:
#         print(f"A[{a.index(i)}] = {i}") #index sorted print nhi ho rhe the
 
