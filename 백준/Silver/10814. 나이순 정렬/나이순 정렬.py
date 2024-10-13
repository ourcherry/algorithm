n = int(input())
arr = []

for i in range(n):
    age, name = input().split()
    arr.append([int(age), name, i])

arr.sort(key = lambda x: (x[0], x[2]))

for item in arr:
    print(item[0], item[1])