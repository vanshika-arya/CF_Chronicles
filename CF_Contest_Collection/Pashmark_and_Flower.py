n = int(input())
b = list(map(int, input().split()))
mn = min(b)
mx = max(b)
if mn == mx:
    ways = n * (n - 1) // 2
else:
    ways = b.count(mn) * b.count(mx)

print(mx - mn, ways)