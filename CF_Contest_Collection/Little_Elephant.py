n = int(input())
a = list(map(int, input().split()))

m = min(a)

if a.count(m) > 1:
    print("Still Rozdil")
else:
    print(a.index(m) + 1)