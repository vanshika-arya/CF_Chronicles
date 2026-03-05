import bisect

n = int(input())
prices = list(map(int, input().split()))
prices.sort()

q = int(input())

for _ in range(q):
    m = int(input())
    print(bisect.bisect_right(prices, m))