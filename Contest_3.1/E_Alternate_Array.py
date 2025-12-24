n = int(input())
a = list(map(int, input().split()))
count1 = 0 
count2 = 0 
for i in range(n):
    if i % 2 == 0:
        if a[i] < 0:
            count1 += 1
        if a[i] > 0:
            count2 += 1
    else:
        if a[i] > 0:
            count1 += 1
        if a[i] < 0:
            count2 += 1
print(min(count1, count2))