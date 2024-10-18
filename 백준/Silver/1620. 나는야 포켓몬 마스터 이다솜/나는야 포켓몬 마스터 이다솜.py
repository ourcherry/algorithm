m, n = map(int, input().split())
pokemon_by_number = {}
pokemon_by_name = {}

for i in range(1, m + 1):
    poke = input().strip()
    pokemon_by_number[i] = poke
    pokemon_by_name[poke] = i
    
for _ in range(n):
    query = input().strip()
    
    if query.isdigit():
        print(pokemon_by_number[int(query)])
    else:
        print(pokemon_by_name[query])
