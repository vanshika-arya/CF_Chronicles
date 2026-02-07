t = int(input())

for case in range(1, t + 1):
    n = int(input())
    
    left = -10**18
    bottom = -10**18
    right = 10**18
    top = 10**18
    
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        left = max(left, x1)
        bottom = max(bottom, y1)
        right = min(right, x2)
        top = min(top, y2)
    
    if left >= right or bottom >= top:
        area = 0
    else:
        area = (right - left) * (top - bottom)
    
    print(f"Case #{case}: {area}")
