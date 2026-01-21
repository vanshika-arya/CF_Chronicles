ra, ca = map(int, input().split())
A = []
for _ in range(ra):
    A.append(list(map(int, input().split())))
rb, cb = map(int, input().split())

B = []
for _ in range(rb):
    B.append(list(map(int, input().split())))
result = [[0 for _ in range(cb)] for _ in range(ra)]
for i in range(ra):
    for j in range(cb):
        for k in range(ca):
            result[i][j] += A[i][k] * B[k][j]
for row in result:
    print(*row)