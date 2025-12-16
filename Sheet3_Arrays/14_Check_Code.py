A,B= map(int,input().split())
s=input()
if s[A] != '-':
    print("No")
else:
    for i in range(len(s)):
        if i!=A:
            if s[i]<'0' or s[i]>'9':
                print("No")
                break
    else:
        print("Yes")
