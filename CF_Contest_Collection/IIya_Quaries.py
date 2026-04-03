s = input().strip()
n = len(s)
pref = [0] * n

for i in range(1, n):
    pref[i] = pref[i-1]
    if s[i] == s[i-1]:
        pref[i] += 1

m = int(input())

for _ in range(m):
    l, r = map(int, input().split())
    print(pref[r-1] - pref[l-1])