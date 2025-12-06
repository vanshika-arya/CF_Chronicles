k=input()
if(k.isdigit()):
    print("IS DIGIT")
else:
    print("ALPHA")
    if(k.isupper()):
        print("IS CAPITAL")
    else:
        print("IS SMALL")