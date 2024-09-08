from collections import deque

direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[-1] * 102 for _ in range(102)]
    visited = [[0] * 102 for _ in range(102)]
    
    fillBoardToRectangle(board, rectangle)
    return bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2, board, visited)
    
def fillBoardToRectangle(board, rectangle):
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    board[i][j] = 0
                elif board[i][j] != 0:
                    board[i][j] = 1 
    
def bfs(start_x, start_y, end_x, end_y, board, visited):
    que = deque()
    que.append((start_x, start_y))
    
    visited[start_x][start_y] = 1
    
    while que:
        x, y = que.popleft()
        
        if (x, y) == (end_x, end_y):
            return visited[x][y] // 2
        
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                que.append((nx, ny))