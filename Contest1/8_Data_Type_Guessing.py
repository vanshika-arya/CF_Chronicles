n, k, a = map(int, input().split())
value_num = n * k
value_den = a  
if value_num % value_den == 0:
    result = value_num // value_den
    if -2147483648 <= result <= 2147483647:
        print("int")
    else:
        print("long long")
else:
    print("double")
