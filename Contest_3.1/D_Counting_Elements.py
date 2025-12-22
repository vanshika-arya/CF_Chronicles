n = int(input())
a = list(map(int, input().split()))
s = set(a)
count = 0
for i in a:
    if i + 1 in s:
        count += 1
print(count)
