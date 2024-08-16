arr = [1, 1, 2, 2, 2, 8] 
sentence = ""

king, queen, look, bishop, night, phone = map(int, input().split())
userInput = [king, queen, look, bishop, night, phone]

for i in range(6):
    sentence += str(arr[i] - userInput[i]) + " "

print(sentence)