n, m = map(int, input().split())
wordlist = []
cnt = 0

for i in range(n):
    wordlist.append(input())
    
for i in range(m):
    if input() in wordlist:
        cnt += 1
        
print(cnt)