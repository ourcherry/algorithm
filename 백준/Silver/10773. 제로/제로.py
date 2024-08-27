n = int(input())
stack = []
sum = 0

for i in range(n):
    num = int(input())
    
    if num == 0 and len(stack) > 0:
        stack.pop()
    else:
        stack.append(num)
        
for item in stack:
    sum += item
    
print(sum)