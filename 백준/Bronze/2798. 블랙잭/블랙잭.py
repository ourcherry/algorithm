cnt, maxnum = map(int, input().split())
numlist = list(map(int, input().split()))
arr = []
tem = 0

for a in numlist:
    
    for b in numlist:
        if a == b:
            continue
        
        for c in numlist:
            if a == c or b == c:
                continue
            
            if a + b + c <= maxnum:
                arr.append(a + b + c)

print(max(arr))