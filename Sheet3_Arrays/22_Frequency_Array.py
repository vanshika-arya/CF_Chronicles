n, m = map(int, input().split())
a = list(map(int, input().split()))
freq = [0] * (m + 1)
for i in a:
    freq[i] += 1
for j in range(1, m + 1):
    print(freq[j])

