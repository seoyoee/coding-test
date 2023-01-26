T = int(input())

for i in range(T):
    answer = 1
    n, m = map(int, input().split())

    for i in range(n):
        answer *= m - i
    for i in range(n):
        answer //= n - i

    print(answer)
