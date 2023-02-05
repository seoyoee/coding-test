import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

answer = 0
s = defaultdict(int)

for i in range(1, n):
    num[i] += num[i - 1]

for i in range(n):
    if num[i] == k:
        answer += 1
    answer += s[num[i] - k]
    s[num[i]] += 1

print(answer)