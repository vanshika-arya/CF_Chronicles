num =input()
N=float(num)
if N.is_integer():
    print(f"int {int(N)}")
else:
    integer,decimal=num.split('.')
    print(f"float {integer} 0.{decimal}")


