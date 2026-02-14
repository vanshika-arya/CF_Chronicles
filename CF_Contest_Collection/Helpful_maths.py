s=input()
a=[]
for i in s:
    if i.isdigit():
        a.append(i)
a.sort()

for j in range(len(a)):

    if j==len(a)-1:
        print(a[j])
    else:
        print(a[j],end='+')
