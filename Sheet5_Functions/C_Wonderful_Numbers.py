n=int(input())
def is_odd(n):
    if n%2!=0:
        return True
    else:
        return False
def binary_Palindrome(n):
    b=bin(n)[2:]
    if b==b[::-1]:
        return True
    else:
        return False
if is_odd(n) and binary_Palindrome(n):
    print("YES")
else:
    print("NO")
