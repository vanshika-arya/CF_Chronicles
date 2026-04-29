t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    count = 0
    for i in range(n - 1):
        if abs(p[i] - p[i + 1]) == 1:
            count += 1
    
    print(count)