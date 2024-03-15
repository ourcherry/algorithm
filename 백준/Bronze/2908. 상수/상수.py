a, b = input().split()

num1 = int(a[2:3] + a[1:2] + a[0:1])
num2 = int(b[2:3] + b[1:2] + b[0:1])

print(num1 if num1 > num2  else num2)