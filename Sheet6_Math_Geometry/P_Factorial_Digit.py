N = int(input())

fact = 1
for i in range(1, N + 1):
    fact = fact * i

digits = 0
while fact > 0:
    digits += 1
    fact //= 10

print("Number of digits of", N, "is", digits)
