while True:
    n,m = map(int,input().split())
    if n<= 0 or m<= 0:
        break
    sum=0
    for i in  range(min(n,m),max(n,m)+1):
        sum+=i
        print(i, end=" ")
    print(f"sum ={sum}")
