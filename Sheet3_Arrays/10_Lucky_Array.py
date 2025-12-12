n=int(input())
a=list(map(int,input().split()))
min=a[0]
for i in a:
    if i<min:
        min=i
count=0
for j in a:
    if j==min:
        count+=1
if count%2!=0:
    print("Lucky")
else:
    print("Unlucky")













































