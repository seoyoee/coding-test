n = int(input())
sizes = []
ranks = [1] * n

for i in range(n):
    sizes.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if sizes[i][0] < sizes[j][0] and sizes[i][1] < sizes[j][1]:
            ranks[i] += 1

for d in ranks:
    print(d, end=" ")