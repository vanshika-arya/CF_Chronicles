n, k = map(int, input().split())
r = list(map(int, input().split()))

y = r[:]
count = 0

for i in range(1, 2*n, 2):
    if count < k and y[i] - 1 < y[i-1] and y[i] - 1 < y[i+1]:
        y[i] -= 1
        count += 1

print(*y)