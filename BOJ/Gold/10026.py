import sys
sys.setrecursionlimit(100000)

n = int(input())
graph1 = []
graph2 = []
for _ in range(n):
    s = input()
    graph1.append(s)
    graph2.append(s.replace('R', 'G'))

def dfs(x, y, graph, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if (x, y) not in visited:
        visited.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == graph[x][y]:
                    dfs(nx, ny, graph, visited)
        return True
    return False

visited1 = []
visited2 = []
answer1 = 0
answer2 = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j, graph1, visited1):
            answer1 += 1
        if dfs(i, j, graph2, visited2):
            answer2 += 1
print(answer1, answer2)