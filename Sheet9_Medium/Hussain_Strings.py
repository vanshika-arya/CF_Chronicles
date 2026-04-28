A = input().strip()
B = input().strip()

if A == B:
    if len(set(A)) < len(A):
        print("YES")
    else:
        print("NO")
else:
    diff = []
    for i in range(len(A)):
        if A[i] != B[i]:
            diff.append(i)


    if len(diff) == 2 and A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]:
        print("YES")
    else:
        print("NO")