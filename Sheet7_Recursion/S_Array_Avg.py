def rec_sum(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + rec_sum(arr, n-1)

n = int(input())
arr = list(map(int, input().split()))

total = rec_sum(arr, n)
print(f"{total/n:.6f}")