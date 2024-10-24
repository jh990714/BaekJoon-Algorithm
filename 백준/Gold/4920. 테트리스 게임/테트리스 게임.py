minimum = float('-inf')

def rotate_90(block):
    rows = len(block)
    cols = len(block[0])
    return [[block[rows - 1 - j][i] for j in range(rows)] for i in range(cols)]

def match(start, block):
    x, y = start
    sum_block = 0

    for i in range(len(block)):
        for j in range(len(block[0])):
            nx = x + i
            ny = y + j

            if not (0 <= nx < n and 0 <= ny < n):
                return minimum

            if not block[i][j]:
                continue

            sum_block += board[nx][ny]

    return sum_block

blocks = [
    [[True, True, True, True]],
    [[True, True, False], [False, True, True]],
    [[True, True, True], [False, False, True]],
    [[True, True, True], [False, True, False]],
    [[True, True], [True, True]]
]

t = 1
while True:
    n = int(input())

    if n == 0:
        break

    board = [list(map(int, input().split())) for _ in range(n)]

    max_block = minimum

    for i in range(n):
        for j in range(n):
            for block in blocks:
                rotated_block = block
       
                for _ in range(4):
                    max_block = max(max_block, match((i, j), rotated_block))
                    rotated_block = rotate_90(rotated_block)

    print(f"{t}. {max_block}")

    t += 1