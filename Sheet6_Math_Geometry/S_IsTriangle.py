import math
a, b, c = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    print("Valid")
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(area)
else:
    print("Invalid")
