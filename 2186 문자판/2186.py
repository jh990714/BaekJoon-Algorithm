import sys

input = sys.stdin.readline

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

N, M, K = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]
word = input().rstrip()

def dfs(x, y, depth):
    if matrix[x][y] != word[depth]:
        return 0
    
    if depth == len(word) - 1:
        return 1
    
    if visited[x][y][depth] != -1:
        return visited[x][y][depth]

    visited[x][y][depth] = 0
    for dx, dy in direction:
        nx = x
        ny = y
        for _ in range(K):
            nx += dx
            ny += dy

            if 0 <= nx < N and 0 <= ny < M:
                visited[x][y][depth] += dfs(nx, ny, depth+1)

    return visited[x][y][depth]

visited = [[[-1 for _ in range(len(word))] for _ in range(M)] for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == word[0]:
            result += dfs(i, j, 0)

print(result)