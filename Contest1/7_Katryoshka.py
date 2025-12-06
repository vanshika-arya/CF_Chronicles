# eye , mouth, body =map(int,input().split())
# Count_KY=0
# while True:
#     if eye>=2 and body>=1:
#         Count_KY+=1
#         eye-=2
#         body-=1
#     elif eye>=2 and body>=1 and mouth>=1:
#         Count_KY+=1
#         eye-=2
#         body-=1
#         mouth-=1
#     elif eye>=1 and body>=1 and mouth>=1:
#         Count_KY+=1
#         eye-=1
#         body-=1
#         mouth-=1
#     else:
#         break
# print(Count_KY)
n, m, k = map(int, input().split())
use_mouth = min(m, k, n)
n -= use_mouth
m -= use_mouth
k -= use_mouth
use_no_mouth = min(n // 2, k)
print(use_mouth + use_no_mouth)
