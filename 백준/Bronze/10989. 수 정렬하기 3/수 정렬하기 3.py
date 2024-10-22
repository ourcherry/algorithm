import sys

n = int(sys.stdin.readline())
count = [0] * 10001  # 0부터 10000까지의 수를 카운트

for _ in range(n):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(10001):
    if count[i] > 0:
        for _ in range(count[i]):
            print(i)
