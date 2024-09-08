from collections import deque

MAX = 1000001

def solution(n, k):
    return bfs(n, k)

def bfs(n, k):
    que = deque()
    que.append(n)
    
    visited = [-1] * MAX

    visited[n] = 0

    while que:
        x = que.popleft()

        if x == k:
            return visited[x]

        for nx in (x*2, x-1, x+1):
            if 0 <= nx < MAX and visited[nx] == -1:
                if nx == x * 2:
                    visited[nx] = visited[x]
                else:
                    visited[nx] = visited[x] + 1
                
                que.append(nx)

n, k = map(int, input().split())
print(solution(n, k))
