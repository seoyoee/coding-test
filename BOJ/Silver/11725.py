import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

def dfs(v):
    for i in graph[v]:
        if not visited[i]:
            visited[i] = v
            dfs(i)

visited = [0] * (n+1)
dfs(1)
print(*visited[2:], sep='\n')