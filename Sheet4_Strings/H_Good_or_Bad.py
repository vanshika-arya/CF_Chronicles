t=int(input())
for i in range(t):
    s=input()
    if s.__contains__("010"):
        print("Good")
    elif s.__contains__("101"):
        print("Good")
    else:
        print("Bad")