square_x = []
square_y = []
cnt = []

for i in range(3):
    a, b = map(int, input().split())
    square_x.append(a)
    square_y.append(b)
    
for item in square_x:
    if square_x.count(item) % 2 != 0:
        cnt.append(item)
        
for item in square_y:
    if square_y.count(item) % 2 != 0:
        cnt.append(item)

print(cnt[0], cnt[1])