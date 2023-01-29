n = int(input())

answer = 0
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i, j in zip(a, b):
    answer += i * j

print(answer)
