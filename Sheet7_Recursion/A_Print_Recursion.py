n=int(input())
def show(n):
    if n==0:
        return
    print("I love Recursion")
    show(n-1)
show(n)