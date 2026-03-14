n = int(input())
a = list(map(int, input().split()))

l, r = 0, n-1
s, d = 0, 0
turn = 0

while l <= r:
    if a[l] > a[r]:
        x = a[l]
        l += 1
    else:
        x = a[r]
        r -= 1

    if turn == 0:
        s += x
    else:
        d += x

    turn = 1 - turn

print(s, d)