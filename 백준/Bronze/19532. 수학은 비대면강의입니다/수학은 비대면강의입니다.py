a, b, c, d, e, f = map(int, input().split())

x = int((b * f - e * c) / (b * d - a * e))
y = int((d * c - a * f) / (b * d - a * e))

print(x, y)