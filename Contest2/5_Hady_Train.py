n = int(input())
row=n//4
col=n%4
if row%2==1:
    col=3-col
print(row,col)
