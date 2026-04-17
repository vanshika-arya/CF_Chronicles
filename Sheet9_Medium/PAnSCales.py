s = input().strip()
extra = input().strip()

left, right = s.split('|')

def weight(x):
    return sum(ord(c) - ord('A') + 1 for c in x)

L = weight(left)
R = weight(right)

extra = list(extra)

for c in extra:
    w = ord(c) - ord('A') + 1
    if L < R:
        left += c
        L += w
    else:
        right += c
        R += w

if L == R:
    print(left + '|' + right)
else:
    print("Impossible")