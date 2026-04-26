import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

for x in arr:
    root = int(math.sqrt(x))
    if root * root == x and is_prime(root):
        print("YES")
    else:
        print("NO")