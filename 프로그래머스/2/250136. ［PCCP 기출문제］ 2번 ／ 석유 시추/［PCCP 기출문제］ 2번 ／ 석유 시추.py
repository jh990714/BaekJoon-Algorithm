from collections import deque

def bfs(x, y, r, c, land, visited, id):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    q = deque()
    q.append((x, y))
    visited[x][y] = id

    cnt = 1
    while q:
        x, y = q.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < r and 0 <= ny < c:
                if land[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = id

                    cnt += 1

    return cnt

def solution(land):
    r, c = len(land), len(land[0])
    group_cnt = {}
    group_id = 1

    # 석유 그룹화
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if land[i][j] == 1 and visited[i][j] == 0:
                cnt = bfs(i, j, r, c, land, visited, group_id)

                group_cnt[group_id] = cnt
                group_id += 1

    answer = 0
    for j in range(c):
        set_group = set()

        for i in range(r):
            if visited[i][j] != 0:
                set_group.add(visited[i][j])
        
        sum_cnt = 0
        for id in set_group:
            sum_cnt += group_cnt[id]

        answer = max(answer, sum_cnt)
        
    return answer