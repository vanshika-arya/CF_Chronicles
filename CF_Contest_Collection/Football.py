n=int(input())
l=[]
for i in range(n):
    s=input()
    l.append(s)
count=0
for i in l:
    p=l.count(i)
    if p>count:
        count=p
        max_t=i
print(max_t)