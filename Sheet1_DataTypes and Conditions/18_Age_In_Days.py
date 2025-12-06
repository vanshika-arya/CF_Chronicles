age=int(input())
year=0
month=0
while age>=365:
    year+=1
    age=age-365
while age>=30:
    month+=1
    age=age-30
print(f"{year} years")
print(f"{month} months")
print(f"{age} days")
