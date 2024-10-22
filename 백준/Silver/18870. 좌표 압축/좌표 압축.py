n = int(input())
arr = list(map(int, input().split()))

arr_set = sorted(set(arr)) 

index_map = {num: idx for idx, num in enumerate(arr_set)}

result = [str(index_map[item]) for item in arr]

print(" ".join(result))