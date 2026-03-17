n = int(input())

full_weeks = n // 7
rem = n % 7
min_days = full_weeks * 2 + max(0, rem - 5)
max_days = full_weeks * 2 + min(2, rem)

print(min_days, max_days)