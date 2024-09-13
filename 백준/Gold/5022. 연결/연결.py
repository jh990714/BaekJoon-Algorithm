from collections import deque

INF = float("inf")
directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
ERROR_MSG = "IMPOSSIBLE"

def solution( a_start, a_end, b_start, b_end):
    result = min(getDist(a_start, a_end, b_start, b_end), getDist(b_start, b_end, a_start, a_end))

    print(result if result != INF else ERROR_MSG)

def getDist(a_start, a_end, b_start, b_end):
    path = [[(0, 0)] * (m+1) for _ in range(n+1)]

    visited = [[-1] * (m+1) for _ in range(n+1)]
    visited[b_start[0]][b_start[1]] = 0
    visited[b_end[0]][b_end[1]] = 0

    first_dist = bfs(a_start, a_end, visited, path)
    if first_dist == INF:
        return INF
    
    visited = [[-1] * (m+1) for _ in range(n+1)]

    drawPath(visited, path, a_start, a_end)

    second_dist = bfs(b_start, b_end, visited, path)
    if second_dist == INF:
        return INF
    
    return first_dist + second_dist

def drawPath(visited, path, start, end):
    cur_path = end
   
    while True:
        visited[cur_path[0]][cur_path[1]] = 0

        if start == cur_path:
            break

        cur_path = path[cur_path[0]][cur_path[1]]

def bfs(start, end, visited, path):
    que = deque()
    que.append(start)

    visited[start[0]][start[1]] = 0

    while que:
        x, y = que.popleft()

        if (x, y) == end:
            return visited[x][y]
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx <= n and 0 <= ny <= m):  # Check if within bounds (0 to n-1 for rows, 0 to m-1 for columns)
                continue

            if visited[nx][ny] != -1:
                continue
            
            visited[nx][ny] = visited[x][y] + 1
            que.append((nx, ny))
            path[nx][ny] = (x, y)

    return INF

if __name__ == "__main__":
    n, m = map(int, input().split())
    a_start = tuple(map(int, input().split()))
    a_end = tuple(map(int, input().split()))
    b_start = tuple(map(int, input().split()))
    b_end = tuple(map(int, input().split()))

    solution(a_start, a_end, b_start, b_end)