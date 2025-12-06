#with the use of elif 
a,b =map(int,input().split())
if a%b==0:
    print("Multiples")
elif b%a==0:
    print("Multiples")
else:
    print("No Multiples")

#with the help of or operator
# if a%b==0 or b%a==0:
#     print("Multiples")
# else:
#     print("No Multiples")

