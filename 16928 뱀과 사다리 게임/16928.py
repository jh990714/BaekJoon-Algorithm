import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

map_size = 101
matrix = [0] * map_size

def bfs():
    visited = [False] * map_size
    visited[1] = True
    q = deque([1])

    while q:
        idx = q.popleft()
        if idx == 100:
            break

        for i in range(1, 7):
            n_idx = idx + i
            
            if n_idx < map_size and visited[n_idx] == False:
                if n_idx in dic.keys():
                    n_idx = dic[n_idx]

                if visited[n_idx] == False:
                    q.append(n_idx)
                    visited[n_idx] = True
                    matrix[n_idx] = matrix[idx] + 1

N, M = map(int, input().split())
dic = {}
for _ in range(N+M):
    u, v = map(int, input().split())
    dic[u] = v


bfs()
print(matrix[-1])