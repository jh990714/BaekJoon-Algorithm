from collections import deque

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solution(board, r, c):
    jh = deque()
    fire = deque()

    visited_jh = [[-1] * c for _ in range(r)]
    visited_fire = [[-1] * c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if board[i][j] == 'J':
                jh.append((i, j))
                visited_jh[i][j] = 0 
                board[i][j] = '.'

            elif board[i][j] == 'F':
                fire.append((i, j))
                visited_fire[i][j] = 0 

    moveFire(fire, board, visited_fire, r, c)
    result = moveJH(jh, board, visited_jh, visited_fire, r, c)

    print(result if result else 'IMPOSSIBLE')


def moveFire(fire: deque, board: list, visited: list, r: int, c: int):
    while fire:
        x, y = fire.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < r and 0 <= ny < c):
                continue

            if visited[nx][ny] != -1 or board[nx][ny] != '.':
                continue

            visited[nx][ny] = visited[x][y] + 1
            fire.append((nx, ny))


def moveJH(jh: deque, board: list, visited_jh: list, visited_fire: list, r: int, c: int):
    while jh:
        x, y = jh.popleft()

        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < r and 0 <= ny < c):
                return visited_jh[x][y] + 1

            if visited_jh[nx][ny] != -1 or board[nx][ny] != '.':
                continue

            if visited_fire[nx][ny] == -1 or visited_jh[x][y] + 1 < visited_fire[nx][ny]:
                visited_jh[nx][ny] = visited_jh[x][y] + 1
                jh.append((nx, ny))

    return None

if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(r)]

    solution(board, r, c)
