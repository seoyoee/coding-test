from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((0, 0))
    
    while queue:
        x, y = queue.popleft()
        print(x, y)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1:
                maps[ny][nx] += maps[y][x]
                queue.append((nx, ny))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]