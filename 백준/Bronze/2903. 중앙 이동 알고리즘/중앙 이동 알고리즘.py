# 2 : 3 -> 5 -> 9 -> 17 -> 33

cal = 2
n = int(input())

for i in range(n):
    cal += cal - 1
    
print(cal * cal)