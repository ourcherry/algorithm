type_cnt, money = map(int, input().split())
type = []
cal_money = money
cnt = 0

for i in range(type_cnt):
    type.append(int(input()))


for j in range(type_cnt):
    item = type[type_cnt - j -1]
    
    n = cal_money // item
    cnt += n
    cal_money = cal_money % item
    
print(cnt)