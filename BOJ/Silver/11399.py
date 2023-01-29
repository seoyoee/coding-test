n = int(input())

answer = 0
time = list(map(int, input().split()))
time.sort()

for i in range(n):
    answer += time[i] * (n - i)

print(answer)