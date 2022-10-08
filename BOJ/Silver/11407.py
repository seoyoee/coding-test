n, k = map(int, input().split())
value = []
count = 0

for i in range(n):
    coin = int(input())
    if coin <= k:
        value.append(coin)
    else:
        break

value.reverse()

while k:
    for i in value:
        count += k // i
        k %= i

print(count)