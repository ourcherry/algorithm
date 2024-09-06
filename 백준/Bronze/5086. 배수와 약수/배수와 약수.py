while True:
    result = "neither"
    a, b = map(int, input().split())
    
    if a == 0 and b == 0:
        break
        
    if a <= b and b % a == 0:
        result = "factor"
    elif a > b and  a % b == 0:
        result = "multiple"
    
    print(result)
    