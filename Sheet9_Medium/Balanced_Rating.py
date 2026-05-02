n = int(input())
a = [int(input()) for _ in range(n)]

b = [x // 2 for x in a]   
diff = -sum(b)          

for i in range(n):
    if a[i] % 2 != 0 and diff > 0:
        b[i] += 1
        diff -= 1

for x in b:
    print(x)