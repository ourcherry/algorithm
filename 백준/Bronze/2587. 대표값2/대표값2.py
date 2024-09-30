arr = []
five = 5

for i in range(five):
    n = int(input())
    arr.append(n)
    
arr.sort()
avg = int(sum(arr) / five)

print(avg)
print(arr[2])