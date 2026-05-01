import math


f1, f2 = input().split()

a, b = map(int, f1.split('/'))
c, d = map(int, f2.split('/'))


lcm_num = (a * c) // math.gcd(a, c)


gcd_den = math.gcd(b, d)


num = lcm_num
den = gcd_den


g = math.gcd(num, den)
num //= g
den //= g

print(f"{num}/{den}")