import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

def floyd_warshall():
    for i in range(1, V+1): # 시작 노드
        for j in range(1, V+1): # 중간 노드
            for k in range(1, V+1): # 종료 노드
                if matrix[i][k] > matrix[i][j] + matrix[j][k]:
                    matrix[i][k] = matrix[i][j] + matrix[j][k]

V, E = map(int, input().split())
matrix = [[INF] * (V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a][b] = c

floyd_warshall()

min_cycle = INF
for i in range(1, V):
    for j in range(i+1, V+1):
        min_cycle = min(min_cycle, matrix[i][i])

if min_cycle == INF:
    print(-1)
else:
    print(min_cycle)