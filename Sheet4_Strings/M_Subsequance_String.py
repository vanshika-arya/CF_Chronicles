# subsequence string
s = input()
target="hello"
temp=0
for i in s:
    if i==target[temp]:
        temp+=1
    if temp==len(target):
        break
if temp==len(target):
    print("YES")
else:
    print("NO")