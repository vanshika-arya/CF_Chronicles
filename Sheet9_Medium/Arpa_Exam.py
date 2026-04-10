n = int(input())

pattern = [8, 4, 2, 6]

if n == 0:
    print(1)
else:
    print(pattern[(n - 1) % 4])