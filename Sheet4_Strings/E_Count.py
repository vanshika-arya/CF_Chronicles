# s=input()
# s=int(s)
# sum=0
# while s>0:
#     sum=sum+s%10
#     s=s//10


# print(sum(s))
s=input()
sum=0
for i in s:
    sum=sum+int(i)
print(sum)