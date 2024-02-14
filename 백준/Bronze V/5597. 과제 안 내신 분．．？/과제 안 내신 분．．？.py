numList = []
absentList = []

for i in range(28):
    numList.append(int(input()))
    
for i in range(30):
    i += 1
    if i not in numList:
        absentList.append(i)

print(absentList[0])
print(absentList[1])