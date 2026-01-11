n=int(input())
a=list(map(int, input().split()))
def min_max(a):
    print(f"{min(a)} {max(a)}")
min_max(a)