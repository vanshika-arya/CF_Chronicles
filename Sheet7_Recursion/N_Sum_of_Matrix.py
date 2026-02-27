def add_matrix(A, B, R, C, i=0, j=0):
    if i == R:
        return
    if j == C:
        print()
        add_matrix(A, B, R, C, i + 1, 0)
        return
    print(A[i][j] + B[i][j], end=" ")
    add_matrix(A, B, R, C, i, j + 1)
R, C = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
B = [list(map(int, input().split())) for _ in range(R)]
add_matrix(A, B, R, C)