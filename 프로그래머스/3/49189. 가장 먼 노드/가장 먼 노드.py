from collections import deque

def bfs(n, start, graph):
    que = deque([start])

    visited = [-1] * (n+1)
    visited[start] = 0
    
    while que:
        u = que.popleft()
        
        for v in graph[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                que.append(v)
    
    max_dist = max(visited)

    return visited.count(max_dist)

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    return bfs(n, 1, graph)