a, b = map(int, input().split())
n = a + b
if n == 0:
    print("NO")
elif n % 2 == 0:
    print("YES" if a == b else "NO")
else:
    print("YES" if abs(a - b) == 1 else "NO")
