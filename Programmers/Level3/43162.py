from collections import deque

def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    
    def bfs(v):
        if computers[v][v]:
            queue = deque([v])
            computers[v][v] = 0
        
            while queue:
                v = queue.popleft()
                for i in range(n):
                    if computers[v][i]:
                        queue.append(i)
                        computers[v][i] = 0
            return True
    
    for i in range(n):
        if bfs(i):
            answer += 1
                
    return answer