import sys
from collections import defaultdict

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    clothes = defaultdict(int)

    for j in range(n):
        v, k = map(str, sys.stdin.readline().split())
        clothes[k] += 1

    answer = 1
    for c in clothes.values():
        answer *= c + 1

    print(answer - 1)
