n_in = int(input())
arr_in = set(map(int, input().split()))  

n_out = int(input())
arr_out = list(map(int, input().split()))

result = []
for item in arr_out:
    if item in arr_in:
        result.append("1")
    else:
        result.append("0")

print(" ".join(result))  
