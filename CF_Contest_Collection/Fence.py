n, k = map(int, input().split())
h = list(map(int, input().split()))

curr_sum = sum(h[:k])
min_sum = curr_sum
index = 0

for i in range(k, n):
    curr_sum += h[i] - h[i - k]
    if curr_sum < min_sum:
        min_sum = curr_sum
        index = i - k + 1

print(index + 1) 