a,b,q = map(int, input().split())
def xor_q(a, b, q):
    if q%3 == 1:
        print(a)
    elif q%3 == 2:
        print(b)
    else:
        print(a ^ b)
xor_q(a, b, q)
