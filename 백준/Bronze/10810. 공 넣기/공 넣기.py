n, m = map(int, input().split())
numList = []
sentence = ""

for i in range(n):
    numList.append(0)

for i in range(m):
    a, b, c = map(int, input().split())
    for i in range(b):
        if i < a-1:
            continue
        numList[i] = c
        
print(' '.join(str(e) for e in numList))