def is_palindrome(arr, left, right):
    if left >= right:
        return True
    if arr[left] != arr[right]:
        return False
    return is_palindrome(arr, left + 1, right - 1)
n = int(input())
arr = list(map(int, input().split()))
if is_palindrome(arr, 0, n - 1):
    print("YES")
else:
    print("NO")