from collections import deque

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    if v1 not in graph[v2]:
        graph[v1].append(v2)
        graph[v2].append(v1)

for node in graph:
    node.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
