T = int(input())
N, X = input().split()
X = int(X)
if T == 1:
    ans = 0
    for ch in N:
        if '0' <= ch <= '9':
            val = ord(ch) - ord('0')
        else:
            val = ord(ch) - ord('A') + 10
        ans = ans * X + val
    print(ans)
else:
    N = int(N)
    if N == 0:
        print(0)
    else:
        res = ""
        while N > 0:
            r = N % X
            if r < 10:
                res = chr(r + ord('0')) + res
            else:
                res = chr(r - 10 + ord('A')) + res
            N //= X
        print(res)
