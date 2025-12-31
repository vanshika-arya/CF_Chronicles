s = input()
count = [0]*26
for c in s:
    count[ord(c)-97] += 1
i = 0
while i < 26:
    if count[i] > 0:
        print(chr(i+97), ":", count[i])
    i += 1


