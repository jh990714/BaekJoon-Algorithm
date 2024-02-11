import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_swan(q):
    next_q = deque()
    
    while q:
        x, y = q.popleft()
        
        if (x, y) == swan[1]:
            return True, next_q

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if visited[nx][ny]:
                   continue 
                
                # 벽과 만나는 지점부터 큐 시작을 위해 값 저장
                if matrix[nx][ny] == 'X':
                    next_q.append((nx, ny))
                else:
                    q.append((nx, ny))
                visited[nx][ny] = True

    return False, next_q

def melt_ice_edges(edges):
    now_edges = set()

    # 가장자리 얼음 녹이기
    for x, y in edges:
        matrix[x][y] = '.'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if matrix[nx][ny] == 'X':
                    now_edges.add((nx, ny))
    
    return now_edges

R, C = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(R)]

edges = set()
swan = []
for i in range(R):
    for j in range(C):
        if matrix[i][j] == '.' or matrix[i][j] == 'L':
            # 처음 가장자리 얼음 구하기
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                
                if 0 <= nx < R and 0 <= ny < C:
                    if matrix[nx][ny] == 'X':
                        edges.add((nx, ny))
        
        if matrix[i][j] == 'L':
            swan.append((i, j))

q = deque()
q.append(swan[0])

visited = [[False] * C for _ in range(R)]
visited[swan[0][0]][swan[0][1]] = True

day = 0
while True:
    # 백조 찾기
    find_check, q = find_swan(q)

    if find_check:
        break
    
    # 가장자리 얼음 녹이기
    edges = melt_ice_edges(edges)
    day += 1

print(day)