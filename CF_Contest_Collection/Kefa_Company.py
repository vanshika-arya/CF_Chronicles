n, d = map(int, input().split())

friends = []
for _ in range(n):
    m, s = map(int, input().split())
    friends.append((m, s))
friends.sort()
l = 0
curr_sum = 0
max_sum = 0
for r in range(n):
    curr_sum += friends[r][1]

    while friends[r][0] - friends[l][0] >= d:
        curr_sum -= friends[l][1]
        l += 1
    max_sum = max(max_sum, curr_sum)
print(max_sum)