x, y, r, n = map(int, input().split())
for _ in range(n):
    xi, yi = map(int, input().split())
    if (xi - x)**2 + (yi - y)**2 <= r**2:
        print("YES")
    else:
        print("NO")
