n=input()
n=int(n)
for i in range(n):
    s,t=input().split()
    i=0
    while i<len(s) and i<len(t):
        print(f"{s[i]}{t[i]}", end="")
        i=i+1
    if i<len(t):
        for j in range(i,len(t)):
            print(t[j],end="")
    else:
        for j in range(i,len(s)):
            print(s[j],end="")
    print()


