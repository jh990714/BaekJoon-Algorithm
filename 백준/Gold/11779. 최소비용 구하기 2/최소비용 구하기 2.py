import heapq

INF = int(1e9)

def solution(n, graph, start, end):
    visited, prev_node = dijkstra(start, graph)

    path = []
    cur_node = end

    while cur_node != -1:
        path.append(cur_node)
        cur_node = prev_node[cur_node]
    
    path.reverse()

    print(visited[end])
    print(len(path))
    print(" ".join(map(str, path))) 

def dijkstra(start, graph):
    que = []
    heapq.heappush(que, (0, start))

    visited = [INF] * (n+1)
    visited[start] = 0
    
    prev_node = [-1] * (n+1)

    while que:
        w, v = heapq.heappop(que)

        if visited[v] < w:
            continue

        for nv, cost in graph[v]:
            new_dist = w + cost
            if visited[nv] > new_dist:
                visited[nv] = new_dist
                prev_node[nv] = v
                heapq.heappush(que, (new_dist, nv))
    return visited, prev_node

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        v, u, w = map(int, input().split())
        graph[v].append((u, w))

    start, end = list(map(int, input().split()))

    solution(n, graph, start, end)