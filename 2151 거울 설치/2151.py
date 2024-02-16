import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(points):
    start = points[0]
    end = points[1]

    q = deque()
    q.append((start[0], start[1], 0, dir))

    while q:
        x, y, cnt, d = q.popleft()

        for dx, dy in d:
            nx = x
            ny = y

            while True:
                nx += dx
                ny += dy

                if nx == end[0] and ny == end[1]:
                    print(cnt)
                    return
                
                if not (0 <= nx < n and 0 <= ny < n) or matrix[nx][ny] == '*':
                    break
                
                if matrix[nx][ny] == '!':
                    n_dir = []
                    if (dx, dy) == dir[0] or (dx, dy) == dir[1]:
                        n_dir.append(dir[2])
                        n_dir.append(dir[3])
                    elif (dx, dy) == dir[2] or (dx, dy) == dir[3]:
                        n_dir.append(dir[0])
                        n_dir.append(dir[1])
                    
                    q.append((nx, ny, cnt+1, n_dir))
                
    
n = int(input())
matrix = [input().rstrip() for _ in range(n)]

points = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == '#':
            points.append((i, j))

bfs(points)