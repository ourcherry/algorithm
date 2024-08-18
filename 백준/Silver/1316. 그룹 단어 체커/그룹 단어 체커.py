num = int(input())
words = [input() for i in range(num)]
cnt = 0

for i in range(len(words)):
    word = words[i]
    arr  = []
    for j in range(len(word)):
        if(word[j] not in arr):
            arr.append(word[j])
        elif(word[j] != word[j-1]):
            break
        if(j + 1 == len(word)):
            cnt += 1
            
print(cnt)