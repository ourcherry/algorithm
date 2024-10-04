a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

result = 0

if c >= a1 and (c - a1) * n0 >= a0:
    result = 1

print(result)