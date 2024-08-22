row, col = map(int, input().split())

arr_first = []
arr_second = []

for a in range(row):
    user_arr = list(map(int, input().split()))
    arr_first.append(user_arr)
    
for n in range(row):
    user_arr = list(map(int, input().split()))
    arr_second.append(user_arr)

for i in range(row):
    for j in range(col):
        arr_first[i][j] += arr_second[i][j]
    
    print(*arr_first[i])