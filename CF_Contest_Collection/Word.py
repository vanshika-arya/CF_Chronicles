s = input().strip()
print(s.upper() if sum(c.isupper() for c in s) > len(s)/2 else s.lower())