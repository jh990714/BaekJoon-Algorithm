import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(points):
    start_x, start_y = points[0]
    end_x, end_y = points[1]

    q = deque()
    q.append((start_x, start_y))

    mir_counts = [[INF] * W for _ in range(H)]
    mir_counts[start_x][start_y] = 0

    while q:
        x, y = q.popleft()

        if x == end_x and y == end_y:
            break

        for i in range(4):
            nx = x
            ny = y

            while True: # 진행방향으로 모두 탐색
                nx += dx[i]
                ny += dy[i]

                if 0 <= nx < H and 0 <= ny < W: 
                    if matrix[nx][ny] == '*': # 벽을 만날 때
                        break
                        
                    if mir_counts[nx][ny] > mir_counts[x][y] + 1: 
                        mir_counts[nx][ny] = mir_counts[x][y] + 1
                        q.append((nx, ny))

                else: # 지도를 벗어날 때
                    break
    
    return mir_counts[end_x][end_y]


W, H = map(int, input().split())
matrix = []
points = []
for i in range(H):
    matrix.append(list(input().rstrip()))

    for j in range(W):
        if matrix[i][j] == 'C':
            points.append((i, j))

print(bfs(points)-1)

