n, b, d = map(int, input().split())
arr = list(map(int, input().split()))

waste = 0
count = 0

for x in arr:
    if x <= b:
        waste += x
        if waste > d:
            count += 1
            waste = 0

print(count)