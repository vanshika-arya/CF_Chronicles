n = int(input())
a = [input() for _ in range(n)]

for i in range(n):
    for j in range(n):
        c = 0
        if i > 0 and a[i-1][j] == 'o': c += 1
        if i < n-1 and a[i+1][j] == 'o': c += 1
        if j > 0 and a[i][j-1] == 'o': c += 1
        if j < n-1 and a[i][j+1] == 'o': c += 1
        if c % 2:
            print("NO")
            exit()

print("YES")