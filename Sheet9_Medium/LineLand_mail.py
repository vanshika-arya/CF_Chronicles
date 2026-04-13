n = int(input())
x = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        mn = x[1] - x[0]
    elif i == n - 1:
        mn = x[n - 1] - x[n - 2]
    else:
        mn = min(x[i] - x[i - 1], x[i + 1] - x[i])
    
    mx = max(x[i] - x[0], x[n - 1] - x[i])
    
    print(mn, mx)