n, k = map(int, input().split())
a = list(map(int, input().split()))
s=0
for i in range(k):
    m = max(a)
    if m <= 0:
        break
    s = s + m
    a.remove(m)
print(s)
