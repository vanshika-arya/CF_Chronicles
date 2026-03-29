def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
fib = [0, 1]
for i in range(2, 51):
    fib.append(fib[i-1] + fib[i-2])

t = int(input())
for _ in range(t):
    n = int(input())
    if is_prime(fib[n]):
        print("prime")
    else:
        print("not prime")