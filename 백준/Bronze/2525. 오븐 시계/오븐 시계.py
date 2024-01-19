h, m = input().split()
d = input()

h = int(h)
m = int(m)
d = int(d)

if m + d >= 60:
    h += (m + d) // 60
    m = (m + d) % 60
else:
    m += d
    
if h >= 24:
    h -= 24

print(h, m)