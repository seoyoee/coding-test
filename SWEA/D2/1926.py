n = int(input())
num = []
for a in range(1, n + 1):
    count = 0
    for i in str(a):
        if int(i) and int(i) % 3 == 0:
            count += 1
    if count:
        num.append("-" * count)
    else:
        num.append(str(a))
print(*num)