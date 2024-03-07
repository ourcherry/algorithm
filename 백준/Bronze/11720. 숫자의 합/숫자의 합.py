n = int(input())
numberSentence = input()
sum = 0

for i in range(n):
    sum += int(numberSentence[i:i+1])
    
print(sum)