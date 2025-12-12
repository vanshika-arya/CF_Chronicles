n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
for i in range(q):
    b = int(input())
    l,r=0,n-1
    while l<=r:
        mid =(l+r)//2
        if a[mid] == b:
            print("found")
            break
        elif a[mid] < b:
            l=mid+1
        else:
            r=mid-1
    else:
        print("not found")
