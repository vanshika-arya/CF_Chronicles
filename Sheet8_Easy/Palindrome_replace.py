s = list(input())
n = len(s)

for i in range(n // 2):
    if s[i] == s[n - i - 1]:
        if s[i] == '?':
            s[i] = s[n - i - 1] = 'a'
    elif s[i] == '?':
        s[i] = s[n - i - 1]
    elif s[n - i - 1] == '?':
        s[n - i - 1] = s[i]
    else:
        print(-1)
        exit()

if n % 2 and s[n // 2] == '?':
    s[n // 2] = 'a'

print("".join(s))