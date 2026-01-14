x,n=map(int,input().split())
def equation(x,n):
    sum=0
    for i in range(0,n+1,2):
        if i==0:
            sum+=(x**0)-1
        else:
            sum+=(x**i)
    print(sum)
equation(x,n)
