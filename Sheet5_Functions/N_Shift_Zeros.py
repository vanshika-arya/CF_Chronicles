n=int(input())
a=list(map(int, input().split()))
def Shift_zeros(a):
    for i in a:
        if i==0:
            a.remove(i)
            a.append(0)
    print(*a)
Shift_zeros(a)