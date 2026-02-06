coords = list(map(int, input().split()))
x_values = coords[0::2]
y_values = coords[1::2]
xmin, xmax = min(x_values), max(x_values)
ymin, ymax = min(y_values), max(y_values)
n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if xmin <= x <= xmax and ymin <= y <= ymax:
        print("YES")
    else:
        print("NO")


