t = int(input())
for i in range(t):
    L,R = map(int, input().split())
    if L>R:
        L,R=R,L
    sR=R*(R+1)//2
    sL=(L-1)*L//2
    print(sR-sL)