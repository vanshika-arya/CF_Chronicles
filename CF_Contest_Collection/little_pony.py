m, n = map(int, input().split())

expected_max = 0.0

for k in range(1, m + 1):
    expected_max += 1 - ((k - 1) / m) ** n

print(expected_max)