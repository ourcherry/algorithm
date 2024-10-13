n = int(input())
arr = []

for i in range(n):
    word = input()
    arr.append(word)

arr = list(set(arr))    
arr.sort(key = lambda x: (len(x), x))

for item in arr:
    print(item)