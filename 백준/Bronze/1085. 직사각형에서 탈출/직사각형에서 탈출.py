x, y, w, h = map(int, input().split())

cal_list = [x, y]
cal_list.append(w - x)
cal_list.append(h - y)

print(min(cal_list))