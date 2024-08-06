from collections import deque

def bfs(n, computers, i, visited):
    que = deque()
    que.append(i)
    
    while que:
        node = que.pop()
        visited[node] = True
        
        for i in range(n):
            if not visited[i] and computers[i][node] and i != node:
                que.append(i)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            answer += 1
            
    return answer