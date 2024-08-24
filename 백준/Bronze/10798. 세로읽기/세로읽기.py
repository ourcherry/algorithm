user_list = []
n = 5
string = ""

for i in range(n):
    user_input = input()
    row_list = []
    
    for j in range(len(user_input)):
        row_list.append(user_input[j])
    
    user_list.append(row_list)

for a in range(max(len(row) for row in user_list)): 
    for b in range(n):
        if a < len(user_list[b]):  
            string += user_list[b][a]
        
print(string)