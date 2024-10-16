n = int(input())
attend = set()

for i in range(n):
    name, inout = input().split()
    
    if inout == "enter":
        attend.add(name)
    elif inout == "leave":
        attend.remove(name)

for item in sorted(attend, reverse=True):
    print(item)