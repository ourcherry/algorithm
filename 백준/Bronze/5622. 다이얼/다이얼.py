arr2 = [3, 'A', 'B', 'C']
arr3 = [4, 'D', 'E', 'F']
arr4 = [5, 'G', 'H', 'I']
arr5 = [6, 'J', 'K', 'L']
arr6 = [7, 'M', 'N', 'O']
arr7 = [8, 'P', 'Q', 'R', 'S']
arr8 = [9, 'T', 'U', 'V']
arr9 = [10, 'W', 'X', 'Y', 'Z']

word = input()
arr = []
time = 0

for i in range(len(word)):
    num = word[i:i+1]
    
    if num in arr2:
        time += arr2[0]
    elif num in arr3:
        time += arr3[0]
    elif num in arr4:
        time += arr4[0]
    elif num in arr5:
        time += arr5[0]
    elif num in arr6:
        time += arr6[0]
    elif num in arr7:
        time += arr7[0]
    elif num in arr8:
        time += arr8[0]
    elif num in arr9:
        time += arr9[0]

print(time)