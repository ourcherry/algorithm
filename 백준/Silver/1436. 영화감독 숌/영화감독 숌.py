n = int(input())
cnt = 0
i = 0

while True:
    i += 1
    str_i = str(i)
    
    if "666" in str_i:
        cnt += 1
        
    if n == cnt:
        print(i)
        break
    