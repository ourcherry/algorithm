n = input()
arr = []
ordered_n = ""

for i in range(len(n)):
    arr.append(n[i])
    
arr.sort(reverse=True)

for item in arr:
    ordered_n += item
    
print(ordered_n)