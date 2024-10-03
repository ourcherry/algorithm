n = int(input())
o = 3

cnt = int(n * (n - 1) * (n - 2) / 6)

if n == 1 or n == 2:
    cnt = 0
    
print(cnt)
print(o)