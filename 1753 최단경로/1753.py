import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(k):
    q = []
    dist[k] = 0
    heapq.heappush(q, (0, k))
    
    while q:
        w, v = heapq.heappop(q)
        if dist[v] < w:
            continue

        for nv, nw in graph[v]:
            if dist[nv] > w + nw:
                dist[nv] = w + nw
                heapq.heappush(q, (w + nw, nv))
    
    return dist

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for i in range(1, V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])