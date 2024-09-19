arr = []
msg = ""

for i in range(3):
    user_input = int(input())
    arr.append(user_input)

a = arr[0]
b = arr[1]
c = arr[2]

if (a + b + c) == 180:
    if a == 60 and b == 60:
        msg = "Equilateral"
    elif a == b or b == c or c == a:
        msg = "Isosceles"
    else:
        msg = "Scalene"
else:
    msg = "Error"
    
print(msg)