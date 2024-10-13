def dfs(u, wires, visited):
    visited[u] = True
    cnt = 1
        
    for v in wires[u]:
        if not visited[v]:
            cnt += dfs(v, wires, visited)
            
    return cnt

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    min_diff = float('inf')
    
    for u, v in wires:
        graph[u].remove(v)
        graph[v].remove(u)
        
        visited = [False] * (n+1)
        
        diff = abs(n - 2 * dfs(u, graph, visited))
        min_diff = min(min_diff, diff)
        
        graph[u].append(v)
        graph[v].append(u)
        
    return min_diff