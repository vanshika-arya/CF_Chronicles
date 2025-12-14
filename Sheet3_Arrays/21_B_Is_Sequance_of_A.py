n,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
i=0
for j in A:
 if i<m and j==B[i]:
  i+=1
print("YES" if i==m else "NO")
