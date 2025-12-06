import math
a,b = map(int, input().split())
div = a/b
floor_val= math.floor(div)
ceil_val=math.ceil(div)
round_val=math.floor(div +0.5)

print(f"floor {a} / {b} = {floor_val}")
print(f"ceil {a} / {b} = {ceil_val}")
print(f"round {a} / {b} = {round_val}")