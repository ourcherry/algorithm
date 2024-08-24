n = 9
arr = []
num = -1
row = 0
col = 0

for i in range(n):
    user_input = list(map(int, input().split()))
    arr.append(user_input)
    
    for j in range(len(user_input)):
        if (user_input[j] > num):
            row = i + 1
            col = j + 1
            num = user_input[j]
            
print(num)
print(row, col)