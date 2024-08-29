arr = [[0 for col in range(100)] for row in range(100)]
cnt = int(input())

for i in range(cnt):
    num_row, num_col = map(int, input().split())
    
    for a in range(10):
        for b in range(10):
            arr[num_row + a][num_col + b] = 1

summary = sum(sum(row) for row in arr)
print(summary)