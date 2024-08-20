word = input()
dic = {}
maxKey = ""
maxNum = 0

for i in range(len(word)):
    spell = word[i].upper()
    if (spell in dic):
        dic[spell] = dic[spell] + 1
    else:
        dic[spell] = 1

for key, value in dic.items():
    if value > maxNum:
        maxNum = value
        maxKey = key
    elif maxNum != 0 and value == maxNum:
        maxKey = "?"

        
print(maxKey)