n = int(input())
a = list(map(int, input().split()))
while len(a)>0:
    print(a[0], end=" ")
    del a[0]
    if len(a)>0:
        print(a[-1], end=" ")
        del a[-1]
