import heapq
def can_transform(a, b):
    if sum(a) != sum(b):
        return "No"
    
    a.sort(reverse=True)
    b = [-x for x in b]
    heapq.heapify(b)
    
    i = 0
    while i < len(a):
        if not b:
            return "No"
        
        x = -heapq.heappop(b)
        
        if x == a[i]:
            i += 1
        elif x < a[i]:
            return "No"
        else:
            heapq.heappush(b, -(x // 2))
            heapq.heappush(b, -(x - x // 2))
    
    return "Yes"

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(can_transform(a, b))