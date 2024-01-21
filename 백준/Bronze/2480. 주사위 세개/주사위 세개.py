a, b, c = map(int, input().split())
m = 0

if a == b and a == c:
    m = a * 1000 + 10000
elif a == b and a != c:
    m = a * 100 + 1000
elif b == c and b != a:
    m = b * 100 + 1000
elif c == a and c != b:
    m = c * 100 + 1000
else: 
    if a > b and a > c:
        m = a * 100
    elif b > a and b > c:
        m = b * 100
    else:
        m = c * 100

print(m)