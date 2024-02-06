n, x = map(int, input().split())
numList = list(map(int, input().split()))
sentence = "";

for i in numList:
    if x > i:
        sentence += str(i) + " "

print(sentence)