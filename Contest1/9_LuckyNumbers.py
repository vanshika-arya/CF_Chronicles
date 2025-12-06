N=input()
N=int(N)
if (N%10!=0 and (N//10)%(N%10)==0 or (N%10)%(N//10)==0):
    print("YES")
else:
    print("NO")

