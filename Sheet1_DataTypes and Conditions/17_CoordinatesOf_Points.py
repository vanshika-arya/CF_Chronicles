# X,Y = map(float,input().split())
# X=float(X)
# Y=float(Y)
# if X>0 and Y>0:
#     print("Q1")
# if X<0 and Y>0:
#     print("Q2")
# if X<0 and Y<0:
#     print("Q3")
# if X>0 and Y<0:
#     print("Q4")
# if X==0 and Y==0:
#     print("Origem")
# if Y==0:
#     print("Eixo X")
# if X==0:
#     print("Eixo Y")

X, Y = map(float, input().split())

if X == 0 and Y == 0:
    print("Origem")
elif X == 0:
    print("Eixo Y")
elif Y == 0:
    print("Eixo X")
elif X > 0 and Y > 0:
    print("Q1")
elif X < 0 and Y > 0:
    print("Q2")
elif X < 0 and Y < 0:
    print("Q3")
else:
    print("Q4")
