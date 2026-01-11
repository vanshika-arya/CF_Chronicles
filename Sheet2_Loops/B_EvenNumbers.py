N=input()
N=int(N)
count=0
for i in range(1,N+1):
    if i%2==0:
        count+=1
        print(i)
if count==0:
    print("-1")