t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    even=0
    odd=0
    for j in a:
        if j % 2==0:
            even += 1
        else:
            odd+=1
    if n%2!= 0:
        print(-1)
    else:
        print(abs(even - odd)//2)
