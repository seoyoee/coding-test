num = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]
answer = [x - y for x, y in zip(chess, num)]
print(*answer)