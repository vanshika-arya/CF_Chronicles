n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
b = c = 0
for i in range(n):
    b+=a[i][i]
    c+=a[i][n-1-i]
print(abs(b-c))
