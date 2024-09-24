status = True

while status:
    arr = list(map(int, input().split()))
    arr.sort()
    a = arr[0]
    b = arr[1]
    c = arr[2]

    if a == b and b == c and c == a:
        if a == 0:
            status = False
            break
        else:
            print("Equilateral")
    
    elif c >= a + b:
        print("Invalid")

    elif a == b or b == c or c == a:
        print("Isosceles")

    elif a != b and b != c and c != a:
        print("Scalene")