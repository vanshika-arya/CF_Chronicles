R, S = map(int, input().split())
if 2*R*R >= S*S:
    print("Circle")
elif S >= 2*R:
    print("Square")
else:
    print("Complex")
