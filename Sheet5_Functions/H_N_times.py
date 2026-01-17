t=int(input())
def n_times(t):
    for i in range(t):
        a,b=input().split()
        a=int(a)
        for j in range(1,a):
            print(b,end=" ")
        print(b)
n_times(t)