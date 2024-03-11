n = int(input())

for i in range(n):
    cnt, word = input().split()
    cnt = int(cnt)
    
    sentence = "";
    for j in range(len(word)):
        sentence += cnt * word[j:j+1]
    
    print(sentence)