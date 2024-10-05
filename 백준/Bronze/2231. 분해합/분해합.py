n = int(input())
result = 0

for i in range(1000000):
    str_i = str(i)
    sum_i = i
    
    for j in range(len(str_i)):
        sum_i += int(str_i[j])
        
    if sum_i == n:
        result = i
        break
    
print(result)