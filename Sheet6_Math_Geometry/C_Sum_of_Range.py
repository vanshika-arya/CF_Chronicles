a,b=map(int,input().split())
s=0
even_s=0
odd_s=0
if a==b:
    for i in range(3):
        print(a)
    exit()
if a<b:
    for i in range(a,b+1):
        s+=i
        if i%2==0:
            even_s+=i
        else:
            odd_s+=i
else:
    for i in range(b,a+1):
        s+=i
        if i%2==0:
            even_s+=i
        else:
            odd_s+=i
print(s)
print(even_s)
print(odd_s)