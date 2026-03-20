n = int(input())
a = list(map(int, input().split()))

pref = [0] * (n + 1)
for i in range(n):
    pref[i+1] = pref[i] + a[i]

b = sorted(a)
pref_sorted = [0] * (n + 1)
for i in range(n):
    pref_sorted[i+1] = pref_sorted[i] + b[i]

m = int(input())
for _ in range(m):
    t, l, r = map(int, input().split())
    
    if t == 1:
        print(pref[r] - pref[l-1])
    else:
        print(pref_sorted[r] - pref_sorted[l-1])