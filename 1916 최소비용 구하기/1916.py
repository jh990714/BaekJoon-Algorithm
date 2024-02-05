import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    dist[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        w, v = heapq.heappop(q)
        
        if dist[v] < w:
            continue

        for nv, nw in graph[v]:
            if dist[nv] > (nw + w):
                dist[nv] = nw + w
                heapq.heappush(q, (nw+w, nv))

N = int(input())
graph = [[] for _ in range(N+1)]
dist = [INF] * (N+1)

M = int(input())
for _ in range(M):
    v, u, w = map(int, input().split())
    graph[v].append((u, w))

start, end = map(int, input().split())

dijkstra(start)

print(dist[end])