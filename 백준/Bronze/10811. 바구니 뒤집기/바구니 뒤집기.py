n, m = map(int, input().split())
numList = list(range(n+1))
numList.remove(0)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    while b - a > 0:
        tmp = numList[a]
        numList[a] = numList[b]
        numList[b] = tmp
        a += 1
        b -= 1
    
print(' '. join(str(i) for i in numList))
