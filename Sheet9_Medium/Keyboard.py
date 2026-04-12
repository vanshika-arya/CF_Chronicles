direction = input().strip()
s = input().strip()

keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"

result = ""

for ch in s:
    idx = keyboard.index(ch)
    if direction == 'R':
        result += keyboard[idx - 1]
    else:
        result += keyboard[idx + 1]

print(result)