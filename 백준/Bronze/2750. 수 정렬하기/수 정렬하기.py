n = int(input())
arr = []

for i in range(n):
    user_input = int(input())
    arr.append(user_input)
    
arr.sort()

for item in arr:
    print(item)