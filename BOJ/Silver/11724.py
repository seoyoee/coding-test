n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v):
    if not visited[v]:
        visited[v] = True
        
        for i in graph[v]:
            dfs(i)
        return True
    return False

visited = [False] * (n+1)
answer = 0
for v in range(1, n+1):
    if dfs(v):
        answer += 1

print(answer)