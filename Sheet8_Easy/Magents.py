n = int(input())
count = 1
prev = input()
for _ in range(n - 1):
    curr = input()
    if curr != prev:
        count += 1
    prev = curr

print(count)