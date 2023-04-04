def dfs(v):
    global answer
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            answer += 1
            dfs(i)

n = int(input())
t = int(input())

graph = [[] for _ in range(n + 1)]
for i in range(t):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)
answer = 0
dfs(1)
print(answer)