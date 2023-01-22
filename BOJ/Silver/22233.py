import sys

n, m = map(int, sys.stdin.readline().split())
memo = []

for i in range(n):
    memo.append(sys.stdin.readline().rstrip())

for i in range(m):
    blog = list(sys.stdin.readline().rstrip().split(","))
    for b in blog:
        if b in memo:
            memo.remove(b)
    print(len(memo))