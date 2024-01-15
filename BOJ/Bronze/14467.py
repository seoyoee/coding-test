n = int(input())
dic = {}
count = 0

for i in range(n):
    num, loc = map(int, input().split())
    if num in dic and dic[num] != loc:
        count += 1
    dic[num] = loc

print(count)