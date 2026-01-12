t=int(input())
Team_a=0
Team_b=0
for i in range(t):
    n=int(input())
    if n==3:
        print("3")
    elif n==2:
        print("2")
    elif n%2==0:
        print("0")
    else:
        print("1")
    
