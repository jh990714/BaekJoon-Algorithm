directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

def fishing(j):
    # print("finshing", j)
    for i in range(R):
        if board[i][j] != 0:
            s, d, z = board[i][j]

            board[i][j] = 0

            # print(z)
            return z

    return 0

def move(i, j, speed, dir):
    if dir == 1 or dir == 2:  # i
        cycle = R * 2 - 2
        if dir == 1:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, 1)
        return (speed, j, 2)

    else:  # j
        cycle = C * 2 - 2
        if dir == 4:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, 4)
        return (i, speed, 3)


def move_shark():
    new_board = [[0] * (C) for _ in range(R)]
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                continue

            s, d, z = board[i][j]
            x, y, d = move(i, j, s, d)

            if new_board[x][y] == 0 or new_board[x][y][2] < z:
                new_board[x][y] = (s, d, z)

    return new_board
R, C, M = map(int, input().split())

board = [[0] * (C) for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())

    board[r-1][c-1] = (s, d, z)

answer = 0
# print(board)
for j in range(C):
    answer += fishing(j)
    board = move_shark()

    # print(board)

print(answer)