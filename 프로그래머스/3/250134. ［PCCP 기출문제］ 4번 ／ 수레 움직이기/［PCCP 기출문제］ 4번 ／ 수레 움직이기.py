def solution(maze):
    answer = set()

    n = len(maze)
    m = len(maze[0])

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    r_cur = ()
    b_cur = ()

    r_end = ()
    b_end = ()
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                maze[i][j] = 0
                r_cur = (i, j)
            elif maze[i][j] == 2:
                maze[i][j] = 0
                b_cur = (i, j)
            elif maze[i][j] == 3:
                r_end = (i, j)
            elif maze[i][j] == 4:
                b_end = (i, j)
    
    r_visited = [[False] * m for _ in range(n)]
    r_visited[r_cur[0]][r_cur[1]] = True

    b_visited = [[False] * m for _ in range(n)]
    b_visited[b_cur[0]][b_cur[1]] = True

    def dfs(r_cur, b_cur, r_visited, b_visited, cnt):
        if r_cur == r_end and b_cur == b_end:
            return cnt

        for dx, dy in direction:
            r_nx = r_cur[0] + dx
            r_ny = r_cur[1] + dy

            if r_cur == r_end:
                r_nx = r_cur[0]
                r_ny = r_cur[1]
                
                r_visited[r_nx][r_ny] = False
                
            if not (0 <= r_nx < n and 0 <= r_ny < m):
                continue

            if maze[r_nx][r_ny] == 5:
                continue

            if r_visited[r_nx][r_ny]:
                continue

            r_visited[r_nx][r_ny] = True
            for dx, dy in direction:
                b_nx = b_cur[0] + dx
                b_ny = b_cur[1] + dy

                if b_cur == b_end:
                    b_nx = b_cur[0]
                    b_ny = b_cur[1]

                    b_visited[b_nx][b_ny] = False

                if not (0 <= b_nx < n and 0 <= b_ny < m):
                    continue
                
                if (r_nx, r_ny) == b_cur and (b_nx, b_ny) == r_cur :
                    continue

                if (b_nx, b_ny) == (r_nx, r_ny):
                    continue

                if maze[b_nx][b_ny] == 5:
                    continue

                if b_visited[b_nx][b_ny]:
                    continue

                b_visited[b_nx][b_ny] = True

                result = dfs((r_nx, r_ny), (b_nx, b_ny), r_visited, b_visited, cnt+1)
                if result is not None:
                    answer.add(result)

                b_visited[b_nx][b_ny] = False

                if b_cur == b_end:
                    break
            
            r_visited[r_nx][r_ny] = False
            
            if r_cur == r_end:
                break

    dfs(r_cur, b_cur, r_visited, b_visited, 0)

    return min(answer) if answer else 0