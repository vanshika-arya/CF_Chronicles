# a,b=map(int,input().split())
# s=0
# even_s=0
# odd_s=0

# if a==b:
#     for i in range(3):
#         print(a)
#     exit()
# if a<b:
#     for i in range(a,b+1):
#         s+=i
#         if i%2==0:
#             even_s+=i
#         else:
#             odd_s+=i
# else:
#     for i in range(b,a+1):
#         s+=i
#         if i%2==0:
#             even_s+=i
#         else:
#             odd_s+=i
# print(s)
# print(even_s)
# print(odd_s)
A,B=map(int, input().split())
l,r=min(A, B),max(A, B)
total = (l + r) * (r - l + 1) // 2
first_even = l if l % 2 == 0 else l + 1
last_even = r if r % 2 == 0 else r - 1
if first_even > last_even:
    even_sum = 0
else:
    n = (last_even - first_even) // 2 + 1
    even_sum = n * (first_even + last_even) // 2
odd_sum = total - even_sum
print(total)
print(even_sum)
print(odd_sum)

