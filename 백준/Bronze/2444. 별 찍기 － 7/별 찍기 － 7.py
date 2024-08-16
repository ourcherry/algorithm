num = int(input())

for i in range(num + 1):
    if (i == 0): 
        continue
    print(" " * (num - i) + "*" * (i * 2 -1))
for i in range(num - 1):
    print(" " * (i + 1)  + "*" * ((num - i - 1) * 2 - 1))