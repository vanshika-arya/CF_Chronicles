# n=int(input())
# l=[]
# while n>0:
#     rem=n%2
#     l.append(rem)
#     n=n//2
# l.reverse()
# one_count = 0
# for j in l:
#     if j == 1:
#         one_count += 1
# ans = (2 ** one_count) - 1
# print(ans)

t = int(input()) 
for i in range(t):
    n=int(input())  
    l=[]
    temp=n
    while temp > 0:
        rem = temp % 2
        l.append(rem)
        temp = temp // 2
    l.reverse()
    one_count = 0
    for j in l:
        if j == 1:
            one_count += 1
    ans = (2 ** one_count) - 1
    print(ans)














# t = int(input())
# for i in range(t):
#     n=int(input())
#     ones=0
#     while n>0:
#         ones+=n&1
#         n>>=1
#     print((1<<ones)-1)

