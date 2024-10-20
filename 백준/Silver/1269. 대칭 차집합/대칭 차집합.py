a, b = map(int, input().split())
set_a = set(input().split())
set_b = set(input().split())

diffrence_set = set_a ^ set_b

print(len(diffrence_set))