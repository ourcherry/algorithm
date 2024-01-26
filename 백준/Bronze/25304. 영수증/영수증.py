sum = 0
total = int(input())
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    sum += a * b
    
if sum == total:
    print("Yes")
else:
    print("No")