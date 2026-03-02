n = int(input())
a = list(map(int, input().split()))

max_i = a.index(max(a))                 
min_i = n - 1 - a[::-1].index(min(a)) 

swaps = max_i + (n - 1 - min_i)

if min_i < max_i:
    swaps -= 1

print(swaps)