A,S,B,Q,C=input().split()
A=int(A)
B=int(B)
C=int(C)
if S=='+':
    if A+B==C:
        print("Yes")
    else:
        print(A+B)
elif S=='-':
    if A-B==C:
        print("Yes")
    else:
        print(A-B)
elif S=='*':
    if A*B==C:
        print("Yes")
    else:
        print(A*B)