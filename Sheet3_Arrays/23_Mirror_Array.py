n, m = map(int, input().split())
for i in range(n):
    row = list(map(int, input().split()))
    row.reverse() 
    print(*row)
