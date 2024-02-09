import sys

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

matrix = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    matrix[i][i] = 0

for _ in range(m):
    u, v, w = map(int, input().split())
    
    if matrix[u][v] > w:
        matrix[u][v] = w

for k in range(1, n+1): # 중간 노드
    for i in range(1, n+1): # 시작 노드
        for j in range(1, n+1): # 도착 노드
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]


for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == INF:
            print(0, end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()