n=int(input())
def show(n):
    if n==1:
        print(n)
        return
    print(n, end=" ")
    show(n-1)
show(n)