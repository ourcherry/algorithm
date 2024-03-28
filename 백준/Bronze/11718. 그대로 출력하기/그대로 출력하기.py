import sys

boolstop = False
arr = []

while not boolstop:
    sen = sys.stdin.readline().strip()
    if sen.strip() == "":
        boolstop = True
        break
    arr.append(sen)

for i in range(len(arr)):
    print(arr[i])