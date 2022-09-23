import math

progresses = list(map(int, input().split()))
speeds = list(map(int, input().split()))

n = len(progresses)
days = []
answer = []
count = 1
    
for i in range(n):
    days.append(math.ceil((100 - progresses[i]) / speeds[i]))

i = 0
while i <= (n - 1):
    j = 1
    if i == (n - 1):
        answer.append(count)
        break
    while days[i] > days[i + j]:
        count += 1
        j += 1
        if i + j == n:
            break
    answer.append(count)
    i += j
    count = 1

print(answer)