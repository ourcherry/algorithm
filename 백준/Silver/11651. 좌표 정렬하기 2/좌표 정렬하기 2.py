n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
    
arr.sort(key=lambda x:(x[1], x[0]))

for item in arr:
    print(item[0], item[1])