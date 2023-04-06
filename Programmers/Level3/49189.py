from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    queue = deque([1])
    distance = [0] * (n+1)
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i != 1 and distance[i] == 0:
                queue.append(i)
                distance[i] = distance[v] + 1

    return distance.count(max(distance))