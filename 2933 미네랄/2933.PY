import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def throw_stic(height, right):
    x = R - height

    if right: # 왼->오른쪽으로 던짐
        for y in range(C):
            if matrix[x][y] == 'x':
                matrix[x][y] = '.'
                
                break
    else: # 오른->왼쪽으로 던짐
        for y in range(C-1, -1, -1):
            if matrix[x][y] == 'x':
                matrix[x][y] = '.'

                break
    
    check_list = deque()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if matrix[nx][ny] == 'x':
                check_list.append((nx, ny))

    drop_check(check_list)
        
def drop_check(check_list):
    while check_list:
        x, y = check_list.popleft()

        drop_list, visited = bfs(x, y)
        if drop_list is not None:
            drop_mineral(drop_list, visited)

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True
    
    drop_list = []
    while q:
        x, y = q.popleft()

        if x == R-1:
            return None, None
        
        if matrix[x+1][y] == '.':
            drop_list.append((x, y))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if not visited[nx][ny] and matrix[nx][ny] == 'x':
                    q.append((nx, ny))
                    visited[nx][ny] = True

    return drop_list, visited

def drop_mineral(drop_list, visited):
    cnt = 1
    check = False
    while True:
        for x, y in drop_list:
            nx = x + cnt

            if nx == R - 1:
                check = True
                break

            if matrix[nx+1][y] == 'x' and  not visited[nx+1][y]:
                check = True
                break
        
        if check:
            break

        cnt += 1

    for i in range(R-1, -1, -1):
        for j in range(C):
            if matrix[i][j] == 'x' and visited[i][j]:
                matrix[i][j] = '.'
                matrix[i+cnt][j] = 'x'

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]
N = int(input())
throw_heights = [*map(int, input().split())]

right = True
for height in throw_heights:
    throw_stic(height, right)
    if right:
        right = False

    else:
        right = True
    
for i in matrix:
    print(''.join(i))