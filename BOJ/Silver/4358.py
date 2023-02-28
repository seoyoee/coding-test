import sys
from collections import defaultdict
tree = sys.stdin.readline().rstrip()
trees = defaultdict(int)
count = 0

while tree:
    trees[tree] += 1
    tree = sys.stdin.readline().rstrip()
    count += 1

trees = sorted(trees.items())

for tree in trees:
    print("%s %.4f" % (tree[0], (tree[1] / count) * 100))