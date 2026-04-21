n, m = map(int, input().split())

marks = [input().strip() for _ in range(n)]

max_marks = [max(marks[i][j] for i in range(n)) for j in range(m)]

count = 0

for i in range(n):
    for j in range(m):
        if marks[i][j] == max_marks[j]:
            count += 1
            break

print(count)