s = input()
count = 0
for i in range(len(s)):
    if s[i].isalpha() and (i == 0 or not s[i-1].isalpha()):
        count += 1
print(count)

