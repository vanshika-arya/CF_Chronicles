n = int(input())
arr = list(map(int, input().split()))

from collections import Counter

freq = Counter(arr)
max_freq = max(freq.values())

if max_freq <= (n + 1) // 2:
    print("YES")
else:
    print("NO")