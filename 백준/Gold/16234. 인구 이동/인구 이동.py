import sys
from collections import deque
input = sys.stdin.readline

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def bfs(point, city, visited):
    que = deque([point])
    visited[point[0]][point[1]] = True
    path = [point]
    
    sum_city = city[i][j]
    while que:
        x, y = que.popleft()

        for dx, dy in direction:
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue
            
            if l <= abs(city[x][y] - city[nx][ny]) <= r:
                visited[nx][ny] = True
                path.append((nx, ny))
                que.append((nx, ny))

                sum_city += city[nx][ny]

    avg = sum_city // len(path)
    return path, avg

def move_city(city, path, avg):
    for x, y in path:
        city[x][y] = avg


n, l, r = map(int, input().split())

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))


cnt = 0
while True:
    visited = [[False] * n for _ in range(n)]
    check = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                path, avg = bfs((i, j), city, visited)

                if len(path) > 1:
                    move_city(city, path, avg)
                    check = True  
    if not check:
        break

    cnt += 1

print(cnt)