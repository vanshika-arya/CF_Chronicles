n = int(input())
i = 2
first = True
while i * i <= n:
    count = 0
    while n % i == 0:
        n //= i
        count += 1
    if count > 0:
        if not first:
            print("*", end="")
        print(f"({i}^{count})", end="")
        first = False
    i += 1
if n > 1:
    if not first:
        print("*", end="")
    print(f"({n}^1)", end="")

