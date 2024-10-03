import sys

n = int(input())
arr = []

for i in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)
    
arr.sort()

for num in arr:
    print(num)