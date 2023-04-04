n = int(input())
house = []

for _ in range(n):
    house.append(list(map(int, input())))

def dfs(x, y):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if house[x][y] == 1:
        house[x][y] = 0
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and house[nx][ny] == 1:
                dfs(nx, ny)
        return True
    return False

answer = []
for i in range(n):
    for j in range(n):
        count = 0
        if dfs(i, j):
            answer.append(count)

answer.sort()
print(len(answer))
for i in answer:
    print(i)