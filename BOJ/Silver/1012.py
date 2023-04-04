import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if graph[x][y]:
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny]:
                dfs(nx, ny)
        return True
    return False

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    count = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j):
                count += 1
    
    print(count)