import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited[x][y] = group
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
    
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if matrix[nx][ny] == '0' and visited[nx][ny] == 0 :
                    q.append((nx, ny))
                    visited[nx][ny] = group
    return cnt

def connect_group_count(x, y):
    cnt = 1
    groups = set()

    for dx, dy in direction:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] != 0:
                groups.add(visited[nx][ny])

    for group in groups:
        cnt += group_cnt[group]

    result[x][y] = cnt % 10


N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
result = [[0] * M for _ in range(N)]

group = 1
group_cnt = {}
wall = []

# 빈칸에서 이동할 수 있는 칸 수 확인
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '0':
            if visited[i][j] == 0:
                cnt = bfs(i, j)
                group_cnt[group] = cnt
                group += 1

        else:
            wall.append((i,j))

# 벽에 인접한 빈칸의 수 확인
for x, y in wall: 
    connect_group_count(x, y)

for i in result:
    print(''.join(map(str, i)))