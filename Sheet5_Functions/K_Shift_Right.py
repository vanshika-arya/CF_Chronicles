def shift_right(arr, n, x):
    x = x % n
    return arr[-x:] + arr[:-x]
n, x = map(int, input().split())
arr = list(map(int, input().split()))
result = shift_right(arr, n, x)
for i in result:
    print(i, end=" ")
