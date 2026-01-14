n=int(input())
if n<=1:
    print("NO")
    exit()
for j in range(2, int(n**0.5)+1):
    if n%j==0:
        print("NO")
        break
else:
    print("YES")