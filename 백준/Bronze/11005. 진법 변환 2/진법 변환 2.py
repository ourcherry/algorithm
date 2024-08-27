digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
          'U', 'V', 'W', 'X', 'Y', 'Z'] # 36

def convert(num, base):
    result = ''
    
    while num > 0:
        num, remainder = divmod(num, base)
        result = digits[remainder] + result
        
    return result
    
a, b = map(int, input().split())
print(convert(a, b))