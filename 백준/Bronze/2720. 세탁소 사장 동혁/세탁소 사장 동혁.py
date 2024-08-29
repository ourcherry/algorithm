querter = 25
dime = 10
nickel = 5
penny = 1
change = [querter, dime, nickel, penny]

t = int(input())

for i in range(t):
    money = int(input())
    result = ""
    
    for c in change:
        result += str(money // c) + " "
        money = money % c
    
    print(result)