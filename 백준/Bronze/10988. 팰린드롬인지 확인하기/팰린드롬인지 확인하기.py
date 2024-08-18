userInput = input()
length = len(userInput)
correct = True;

for i in range(length):
    correct = userInput[i] == userInput[length - i - 1]
    if (correct == False):
        break;
        
print(1 if correct else 0);