t=int(input())
for i in range(t):
    h,w=map(int,input().split())
    if h==w:
        print("Square")
    else:
        print("Rectangle")