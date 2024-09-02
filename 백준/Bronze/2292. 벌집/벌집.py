# 1 -> 7 -> 19 -> 37 -> 61 -> 91
# 6 12 18 24
# 1 3 6 10 15

import math

def find_n_from_sum(S):
    n = (1 + math.sqrt(1 + 8 * S)) / 2
    return math.ceil(n)

S = (int(input()) - 1) / 6
n = find_n_from_sum(S) 
print(n)