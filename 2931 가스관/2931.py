import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y, [(-1, 0), (1, 0), (0, -1), (0, 1)]))

    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True

    blanks = []
    while q:
        x, y, dir = q.popleft()

        for dx, dy in dir:
            nx = x + dx
            ny = y + dy

            
            if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == False:
                if matrix[nx][ny] == 'Z':
                    continue

                if matrix[nx][ny] != '.' and matrix[nx][ny]:
                    dir = find_dir(matrix[nx][ny])
                    q.append((nx, ny, dir))
                    visited[nx][ny] = True
                else:
                    blanks.append((nx, ny))
    
    return blanks

# 가르키는 방향
def find_dir(block):
    if block == '|':
        return [(-1, 0), (1, 0)]

    elif block == '-':
        return [(0, -1), (0, 1)]
    
    elif block == '+' or block == 'M' or block == 'Z':
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    elif block == '1':
        return [(1, 0), (0, 1)]
    
    elif block == '2':
        return [(-1, 0), (0, 1)]
    
    elif block == '3':
        return [(-1, 0), (0, -1)]
    
    elif block == '4':
        return [(1, 0), (0, -1)]

R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]

m = ()

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'M':
            m = (i, j)

check_list = bfs(m[0], m[1])

for x, y in check_list:
    pipe_x = []
    pipe_y = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if  0 <= nx < R and 0 <= ny < C and matrix[nx][ny] != '.':
            # M, Z 예외 해줘야 불필요한 파이프가 생기지 않음, 문제가 예매함
            if matrix[nx][ny] == 'M' or matrix[nx][ny] == 'Z':
                continue

            dir = find_dir(matrix[nx][ny])
            if (-dx[i], -dy[i]) in dir: # 방향과 일치하는지 확인
                pipe_x.append(dx[i])
                pipe_y.append(dy[i])
    
    if len(pipe_x) == 0: # 그냥 빈 공간
        continue
    
    result = [x+1, y+1]

    if len(pipe_x) == 2: 
        sum_x = sum(pipe_x)
        sum_y = sum(pipe_y)

        if (sum_x, sum_y) == (1, 1):
            result.append('1')
        elif (sum_x, sum_y) == (-1, 1):
            result.append('2')
        elif (sum_x, sum_y) == (-1, -1):
            result.append('3')
        elif (sum_x, sum_y) == (1, -1):
            result.append('4')
        elif (sum_x, sum_y) == (0, 0):
            if pipe_x[0] == 0:
                result.append('-')
            else:
                result.append('|')    
    elif len(pipe_x) == 4:
        result.append('+')
    
    print(*result)
    break