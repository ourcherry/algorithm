X = int(input())

line = 1
count = 0 

while count < X:
    count += line
    line += 1

line -= 1 
count -= line

index_in_line = X - count

if line % 2 == 0:
    numerator = index_in_line
    denominator = line - index_in_line + 1
else:
    numerator = line - index_in_line + 1
    denominator = index_in_line

print(f"{numerator}/{denominator}")
