def divisor(num, n):
    arr = []
    
    for i in range(num):
        i += 1
        if num % i == 0:
            arr.append(i)
    
    if n > len(arr):
        return 0
    else:
        return arr[n - 1]

a, b = map(int, input().split())
print(divisor(a, b))