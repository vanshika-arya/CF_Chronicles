def swap_matrix(n, x, y, mat):
  
    mat[x-1], mat[y-1] = mat[y-1], mat[x-1]

    for i in range(n):
        mat[i][x-1], mat[i][y-1] = mat[i][y-1], mat[i][x-1]
    
    return mat

n, x, y = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

result = swap_matrix(n, x, y, mat)

for row in result:
    print(*row)