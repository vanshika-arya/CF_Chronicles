n = int(input())
arr = list(map(int, input().split()))

from collections import Counter

freq = Counter(arr)

ans = 0
for v in freq.values():
    if v > 1:
        ans += (v - 1)

print(ans if ans > 0 else -1)