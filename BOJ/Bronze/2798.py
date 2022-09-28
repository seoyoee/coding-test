from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

perm = list(permutations(num, 3))

print(max([sum(x) for x in perm if sum(x) <= m]))