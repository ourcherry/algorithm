triangle = list(map(int, input().split()))
triangle.sort()

a = triangle[0]
b = triangle[1]
c = triangle[2]

if a + b <= c:
    c =  a + b - 1
    
print(a + b + c)