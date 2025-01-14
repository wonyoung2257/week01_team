# 순열을 사용하여 모든 가능한 수를 찾음
from itertools import permutations
import sys
sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int ,input().split()))

permu = list(permutations(arr, n))
def calculator(li):
  total = 0
  for i in range(len(li)-1):
    total += abs(li[i]-li[i+1])
  return total

answer = -1e9
for li in permu:
  answer = max(answer, calculator(li))

print(answer)
