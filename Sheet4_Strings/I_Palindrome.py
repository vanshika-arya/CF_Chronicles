s=input()
l=0
r=len(s)-1
while l<r:
    if s[l]!=s[r]:
        print("NO")
        exit()
    l=l+1
    r=r-1
print("YES")