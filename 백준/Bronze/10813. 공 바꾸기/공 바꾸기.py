basket = []
temp = 0

n, m = map(int, input().split())

for i in range(n):
    basket.append(i + 1)

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    
    temp = basket[a]
    basket[a] = basket[b]
    basket[b] = temp

print(' '.join(str(e) for e in basket))
    