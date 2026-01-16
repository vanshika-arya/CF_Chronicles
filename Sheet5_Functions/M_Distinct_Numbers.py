n=int(input())
a=map(int, input().split())
def count(a):
    total=0
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
            total+=1
    print(total)
count(a)
