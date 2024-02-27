from collections import deque
import heapq

direction = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]

def bfs(n, m, x, y, r, c, k):
    q = []
    heapq.heappush(q, ("", x, y))

    while q:
        path, x, y = heapq.heappop(q)
        
        
        if (x, y) == (r, c):
            if len(path) == k:
                return path
            
            if (k - len(path)) % 2 == 1:
                return "impossible"
            
        for dx, dy, s in direction:
            nx = x + dx
            ny = y + dy

            if 1 <= nx <= n and 1 <= ny <= m: 
                distance = abs(r - nx) + abs(c - ny)
                if distance > (k - len(path) - 1):
                    continue
                    
                heapq.heappush(q, (path+s, nx, ny))

    return "impossible"

def solution(n, m, x, y, r, c, k):
    answer = bfs(n, m, x, y, r, c, k)

    return answer