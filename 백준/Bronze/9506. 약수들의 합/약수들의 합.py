def sum_divisor(num):
    arr = []
    str_arr = ""
    
    for i in range(num):
        i += 1
        if num % i == 0 and i != num:
            arr.append(i)
            if i == 1:
                str_arr += str(i)
            else:
                str_arr += " + " + str(i)
            
    
    if sum(arr) == num:
        print(f"{num} = {str_arr}")
    else:
        print(f"{num} is NOT perfect.")


while True:
    n = int(input())
    
    if n == -1:
        break
    
    sum_divisor(n)