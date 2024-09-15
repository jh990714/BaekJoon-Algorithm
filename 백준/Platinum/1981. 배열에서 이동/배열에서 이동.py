from collections import deque

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
MIN = 0
MAX = 200

def bfs(low, high):
    que = deque()
    que.append((0, 0))

    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while que:
        x, y = que.popleft()

        if (x, y) == (n-1, n-1):
            return True
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            if low <= board[nx][ny] <= high:
                que.append((nx, ny))
                visited[nx][ny] = True

    return False

def check(mid):
    for low in range(MAX + 1):
        high = low + mid
        
        if high > MAX:
            continue

        if not (low <= board[0][0] <= high and low <= board[n-1][n-1] <= high):
            continue

        if bfs(low, high):
            return True
        
    return False

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

left = MIN
right = MAX
result = 0

while left < right:
    mid = (left + right) // 2

    if check(mid):
        right = mid
    else:
        left = mid + 1

print(right)