import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[-1] * w for _ in range(h)]
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if room[nx][ny] != "x" and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    room = [list(input().rstrip()) for _ in range(h)]

    # 청소기, 더러운 칸 위치 찾기
    cleaner = ()
    dirty_pos = []
    
    for i in range(h):
        for j in range(w):
            if room[i][j] == 'o': # 청소기 위치
                cleaner = (i, j)
            elif room[i][j] == '*': # 더러운 칸 위치
                dirty_pos.append((i, j))
    
    graph = [[INF] * (len(dirty_pos)+1) for _ in range(len(dirty_pos)+1)]
    
    # 청소기 -> 더러운 칸간의 거리
    visited = bfs(cleaner[0], cleaner[1])
    visit_check = True
    for i in range(len(dirty_pos)):
        x, y = dirty_pos[i]

        if visited[x][y] == -1:
            visit_check = False
            break
        
        graph[0][i+1] = visited[x][y]

    if not visit_check:
        print(-1)
        continue
    
    # 더러운 칸 - 더러운 칸간의 거리
    for j, pos in enumerate(dirty_pos):
        visited = bfs(pos[0], pos[1])

        for i in range(len(dirty_pos)):
            x, y = dirty_pos[i]
            
            graph[j+1][i+1] = visited[x][y]
    
    # 청소기부터 시작해서 모든 노드를 잇는 최소 신장 트리
    from itertools import permutations

    min_distance = INF
    for perm in permutations(range(1, len(dirty_pos)+1)):
        distance = graph[0][perm[0]] # 청소기로부터 첫 번째 더러운 칸까지의 거리
        for i in range(len(perm)-1):
            distance += graph[perm[i]][perm[i+1]] # 더러운 칸 간의 거리
        min_distance = min(min_distance, distance)

    print(min_distance)

