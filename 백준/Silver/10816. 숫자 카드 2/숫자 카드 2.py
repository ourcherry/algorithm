import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

c = Counter(cards)
print(" ".join(str(c[q]) for q in queries))