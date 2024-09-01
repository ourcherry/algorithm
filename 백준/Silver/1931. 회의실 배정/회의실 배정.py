n = int(input())
meetings = []

for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
current_end = 0

for start, end in meetings:
    if start >= current_end:
        count += 1
        current_end = end

print(count)
