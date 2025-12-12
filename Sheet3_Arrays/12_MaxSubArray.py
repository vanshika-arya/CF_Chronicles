t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    res = []
    for l in range(1, n+1):
        for start in range(n-l + 1):
            max = a[start]
            for k in range(start+1, start+l):
                if a[k] > max:
                    max = a[k]
            res.append(max)
    print(*res)


