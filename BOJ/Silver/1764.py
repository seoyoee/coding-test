n, m = map(int, input().split())

unheard = set()
unseen = set()

for i in range(n):
    unheard.add(input())

for i in range(m):
    unseen.add(input())

answer = unseen.intersection(unheard)
answer = sorted(answer)

print(len(answer))
for p in answer:
    print(p)
