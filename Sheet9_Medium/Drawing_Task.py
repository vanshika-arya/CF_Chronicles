n, m, q = map(int, input().split())
grid = [['.' for _ in range(m)] for _ in range(n)]
for _ in range(q):
    r1, c1, r2, c2, ch = input().split()
    r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
    for i in range(r1 - 1, r2):
        for j in range(c1 - 1, c2):
            grid[i][j] = ch
for row in grid:
    print(''.join(row))