import sys

input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    # deque시 시간초과 --> set으로 중복제거 
    q = set()
    q.add((x, y, matrix[x][y]))
    max_len = 1
    while q:
        x, y, log = q.pop()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if matrix[nx][ny] not in log:
                    q.add((nx, ny, log + matrix[nx][ny]))
                    max_len = max(max_len, len(log)+1)
    else:
        return max_len
    
R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]

print(bfs(0, 0))