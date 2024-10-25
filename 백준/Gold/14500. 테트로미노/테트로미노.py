tetrominos = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # 막대 모양
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # 정사각형
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L 모양
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z 모양
    [(0, 0), (0, 1), (0, 2), (1, 1)]   # T 모양
]

MIN = float('-inf')

def rotate_90(block):
    return [(y, -x) for x, y in block]

def reflect(block):
    return [(-x, y) for x, y in block]

def generate_all_shapes(tetromino):
    shapes = []
    current = tetromino

    for _ in range(4):
        current = rotate_90(current)
        shapes.append(current)
        shapes.append(reflect(current))
    return shapes

def match(board, i, j, block):
    total = 0
    for x, y in block:
        nx, ny = i + x, j + y

        if not (0 <= nx < n and 0 <= ny < m):
            return MIN

        total += board[nx][ny]

    return total

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

all_shapes = [generate_all_shapes(tetromino) for tetromino in tetrominos]

max_total = MIN

for i in range(n):
    for j in range(m):
        for shapes in all_shapes:
            for shape in shapes:
                max_total = max(max_total, match(board, i, j, shape))

print(max_total)