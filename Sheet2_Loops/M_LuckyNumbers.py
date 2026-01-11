A, B = map(int, input().split())
n=0
for num in range(A, B + 1):
    s = str(num)
    for ch in s:
        if ch!='4' and ch!='7':
            break
    else:
        print(num, end=" ")
        n=1
if n==0:
    print(-1)
