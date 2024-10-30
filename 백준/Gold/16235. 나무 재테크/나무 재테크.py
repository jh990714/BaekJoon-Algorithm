from collections import deque

directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def spring():
    for i in range(N):
        for j in range(N):
            len_tree = len(trees[i][j])

            for k in range(len_tree):
                if board[i][j] >= trees[i][j][k]:
                    board[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                else:
                    for _ in range(k, len_tree):
                        die_trees[i][j].append(trees[i][j].pop())
                    break

def summer():
    for i in range(N):
        for j in range(N):
            while die_trees[i][j]:
                board[i][j] += die_trees[i][j].pop() // 2

def fall():
    for i in range(N):
        for j in range(N):
            len_tree = len(trees[i][j])

            for k in range(len_tree):
                if trees[i][j][k] % 5 == 0:
                    for dx, dy in directions:
                        nx, ny = i + dx, j + dy

                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)

def winter():
    for i in range(N):
        for j in range(N):
            board[i][j] += input_board[i][j]

N, M, K = map(int, input().split())

input_board = []
trees = [[deque() for _ in range(N)] for _ in range(N)]
board = [[5] * N for _ in range(N)]
die_trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(N):
    input_board.append(list(map(int, input().split())))

for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    spring()
    summer()
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(trees[i][j])

print(answer)