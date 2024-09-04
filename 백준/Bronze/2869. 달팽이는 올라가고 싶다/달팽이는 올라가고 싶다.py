# 반례 10 9 11

import math

day, night, tree = map(int, input().split())

l = day - night
m = tree - day

cnt = math.ceil(m / l) + 1

if tree <= day:
    cnt = 1

print(cnt)