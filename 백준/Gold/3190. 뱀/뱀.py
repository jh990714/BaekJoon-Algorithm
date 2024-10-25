from collections import deque

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
max_time = 10000

def move(snake, cur_dir):
    nx = snake[-1][0] + directions[cur_dir][0]
    ny = snake[-1][1] + directions[cur_dir][1]

    if not (1 <= nx < n+1 and 1 <= ny < n+1):
        return False

    if (nx, ny) in snake:
        return False

    snake.append((nx, ny))
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        snake.popleft()

    return True

def turn(cur_dir, c):
    if c == 'L':
        return (cur_dir + 1) % 4
    elif c == 'D':
        return (cur_dir - 1) % 4


n = int(input())

k = int(input())
apples = [tuple(map(int, input().split())) for _ in range(k)]

l = int(input())
change_directions = {}
for _ in range(l):
    x, c = input().split()
    change_directions[int(x)] = c

board = [[0] * (n+1) for _ in range(n+1)]
for x, y in apples:
    board[x][y] = 1

cur_dir = 0
cur_t = 0
snake = deque([(1, 1)])
time = 0

while True:
    time += 1

    if not move(snake, cur_dir):
        break

    if time in change_directions:
        cur_dir = turn(cur_dir, change_directions[time])

print(time)