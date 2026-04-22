import math

n = int(input())
arr = list(map(int, input().split()))

s = sum(math.log(x) for x in arr)

z = int(math.exp(s / n)) + 1

print(z)