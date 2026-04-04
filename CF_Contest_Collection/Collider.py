n = int(input())
s = input()
x = list(map(int, input().split()))

ans = float('inf')

for i in range(n - 1):
    if s[i] == 'R' and s[i + 1] == 'L':
        ans = min(ans, (x[i + 1] - x[i]) // 2)

print(ans if ans != float('inf') else -1)