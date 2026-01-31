L, R, M = map(int, input().split())
ans = 1
for i in range(L, R + 1):
    ans = (ans * i) % M
print(ans)
