max = 0
cnt = 0

for i in range(9):
    n = int(input())
    if n > max:
        max = n
        cnt = i + 1

print(max)
print(cnt)