from collections import deque

def bfs(start):
    que = deque([start])
    visited = [-1] * (n+1)
    visited[start] = 0

    while que:
        v = que.popleft()

        for nv, cost in tree[v]:
            if visited[nv] == -1:
                visited[nv] = visited[v] + cost
                que.append(nv)

    max_visited = max(visited)
    
    return visited.index(max_visited), max_visited

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n):
    line = list(map(int, input().split()))
    node = line[0]

    for i in range(1, len(line) - 2, 2):
        tree[node].append((line[i], line[i+1]))

print(bfs(bfs(1)[0])[1])