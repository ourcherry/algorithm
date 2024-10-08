n = int(input())
cnt = -1
max_5 = n // 5


for a in range(max_5):
    a = max_5 - a
    rest = n - (a * 5)
    
    if rest % 3 == 0:
        cnt = a + (rest // 3)
        break
    
if cnt == -1 and n % 3 == 0:
    cnt = n // 3
    
print(cnt)