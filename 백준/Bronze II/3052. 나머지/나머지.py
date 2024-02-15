numDictionary = {}

for i in range(10):
    n = int(input()) % 42
    numDictionary[n] = 'val'
    
distinctList = list(numDictionary.keys())
print(len(distinctList))