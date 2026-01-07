s = input()
l = s.split()
for i in range(len(l)):
    temp = l[i]
    rev = ""
    for j in temp:
        rev = j + rev
    l[i] = rev
print(" ".join(l))
