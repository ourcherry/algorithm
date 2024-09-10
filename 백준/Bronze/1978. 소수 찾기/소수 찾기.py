def is_prime_number(num):
    arr = []
    
    for i in range(num):
        i += 1
        if num % i == 0:
            arr.append(i)
            
    return len(arr) == 2


result = []
n = int(input())
input_list = list(map(int, input().split()))

for i in range(n):
    if is_prime_number(input_list[i]):
        result.append(input_list[i])    

print(len(result))

