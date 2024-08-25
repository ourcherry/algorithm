user_list = []
n = 5
string = ""
max_length = 0

for i in range(n):
    user_input = input()
    row_list = []
    length = len(user_input)
    
    for j in range(length):
        row_list.append(user_input[j])
    
    if max_length < length:
        max_length = length
    
    user_list.append(row_list)

for a in range(max_length): 
    for b in range(n):
        if a < len(user_list[b]):  
            string += user_list[b][a]
        
print(string)