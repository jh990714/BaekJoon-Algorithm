import sys

input = sys.stdin.readline
INF = sys.maxsize

def bellman_f(start):
    dist[start] = 0

    for i in range(1, N+1):
        for j in range(M):
            u, v, w = edges[j]

            if dist[u] != INF and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w

                if i == N:
                    return True
    
    return False

N, M = map(int, input().split())
edges = []
dist = [INF] * (N+1)
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

start_node = 1
cycle_check = bellman_f(start_node)

if cycle_check:
    print(-1)
else:
    for i in range(1, N+1):
        if i == start_node:
            continue

        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
    

