n, m = map(int, input().split())

names = set()
selected_names = []

for _ in range(n):
    name = input()
    names.add(name)

for _ in range(m):
    in_name = input()
    if in_name in names:
        selected_names.append(in_name)

selected_names.sort() 
print(len(selected_names))
for item in selected_names:
    print(item)
