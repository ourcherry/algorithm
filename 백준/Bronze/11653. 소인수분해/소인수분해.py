import sys

n = int(sys.stdin.readline())
rest = n
keep = True
i = 2

while keep:
    if n == 1:
        keep = False
    elif rest <= i:
        print(i)
        keep = False
    elif rest % i == 0:
        print(i)
        rest = rest // i 
    elif i == 2:
        i += 1
    else:
        i += 2
        