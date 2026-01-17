n=int(input())
a=list(map(float, input().split()))
def average_n(a,n):
    sum=0
    for i in a:
        sum+=i
    print(f"{sum/n:.7f}")
average_n(a,n)
