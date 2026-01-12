n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
def new_array(a,b):
    b.extend(a)
    c=b
    print(*c)
new_array(a,b)