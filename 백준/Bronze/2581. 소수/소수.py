def is_prime_number(num):
    arr = []
    
    for i in range(num):
        i += 1
        if num != 1 and num % i == 0:
            arr.append(i)
            
    return len(arr) == 2


result = []
m = int(input())
n = int(input()) + 1

for i in range(n - m):
    i += m
    if is_prime_number(i):
        result.append(i)
        
if len(result) == 0:
    print(-1)
else:
    result.sort()
    print(sum(result))
    print(result[0])