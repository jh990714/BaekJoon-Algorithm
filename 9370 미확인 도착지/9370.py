import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(k):
    q = []
    heapq.heappush(q, (0, k))
    
    dist = [INF] * (n+1)
    dist[k] = 0
    
    while q:
        w, v = heapq.heappop(q)
        if dist[v] < w:
            continue

        for nv, nw in graph[v]:
            if dist[nv] > w + nw:
                dist[nv] = w + nw
                heapq.heappush(q, (dist[nv], nv))
    
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    end_list = []
    for _ in range(t):
        x = int(input())
        end_list.append(x)

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)
    
    result = []
    for end in end_list:
        if dist_s[g] + dist_g[h] + dist_h[end] == dist_s[end] or dist_s[h] + dist_h[g] + dist_g[end] == dist_s[end]:
            result.append(end)

    result.sort()
    print(*result)