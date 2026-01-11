n = int(input())
num = 1
for i in range(n):
    for j in range(1, 5):
        if j == 4:
            print("PUM")
        else:
            print(num, end=" ")
            num+=1
    num+=1
