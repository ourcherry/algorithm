n = int(input())
numList = list(map(int, input().split()))
min = numList[0]
max = numList[0]

for i in numList:
    if i < min:
        min = i
    if i > max:
        max = i
print(min, max)
    