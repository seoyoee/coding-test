n, k = map(int, input().split())

medals = [list(map(int, input().split())) for _ in range(n)]
medals.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

for medal in medals:
    if medal[0] == k:
        arr = medal

for medal in medals:
    if medal[1:] == arr[1:]:
        print(medals.index(medal) + 1)
        break
