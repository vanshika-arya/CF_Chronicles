fib1 = 0
fib2 = 1
n = int(input())
for i in range(n):
    print(fib1, end=" ")
    fibn= fib1 + fib2
    fib1 = fib2
    fib2 = fibn