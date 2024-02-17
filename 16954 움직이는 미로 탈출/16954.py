import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

direction = [(1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)] # 1 2 3 4 5 6 7 8 9
SIZE = 8

def bfs(start, end):
    global wall

    x, y = start
    q = deque()
    q.append((x, y))
    
    time = 0
    while q:
        if time == SIZE: # 8초후면 모든 벽이 없어짐
            return 1
        
        if not wall: # 벽이 존재하지 않을 때
            return 1
        
        # 방문한 곳 계속 초기화 해줘야함
        visited = []
        for _ in range(len(q)):
            x, y = q.popleft()

            if x == end[0] and y == end[1]: # 목적지 도착
                return 1
            
            if (x, y) in wall: # 현재 위치가 벽이면 탐색 안함
                continue

            for dx, dy in direction:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < SIZE and 0 <= ny < SIZE:
                    if (nx, ny) not in wall and (nx, ny) not in visited: # 다음 위치가 벽이 아니고 방문한 적 없을때 추가
                        q.append((nx, ny))
                        visited.append((nx, ny))
        
        # 벽 한칸 이동
        down_wall = []
        for x, y in wall:
            if x + 1  < SIZE:
                down_wall.append((x+1, y))
        
        wall = down_wall
        
        time += 1

    return 0

matrix = [input().rstrip() for _ in range(SIZE)]
start_p = (SIZE-1, 0)
end_p = (0, SIZE-1)
wall = []
for i in range(SIZE):
    for j in range(SIZE):
        if matrix[i][j] == '#':
            wall.append((i, j))

print(bfs(start_p, end_p))