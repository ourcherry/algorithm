n = int(input())
scoreList = list(map(int, input().split()))

sum = 0
maxScore = max(scoreList)

for i in scoreList:
    sum += i

finalScore = round(sum / maxScore * 100 / n, 2)

print(finalScore)
