from collections import deque

def bfs(x, y, maps):
    n, m = len(maps), len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == (n-1, m-1): break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m): continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
    return maps[n-1][m-1]
            
        
        
    

def solution(maps):
    answer = bfs(0, 0, maps)
    
    return answer if answer != 1 else -1