import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

def bfs(min_group, max_group):
    q = deque()
    q.append((min_group, max_group))

    visited = [[False] * (size+1) for _ in range(size+1)]
    visited[min_group][max_group] = True

    while q:
        min_group, max_group = q.popleft()
        diff = size - min_group - max_group

        if max_group == min_group == diff:
            print(1)
            return
        
        for x, y in ((min_group, max_group), (min_group, diff), (max_group, diff)):
            if x > y:
                x -= y
                y += y
            elif x < y:
                y -= x
                x += x
            else:
                continue
            
            i = min(x, y, size-x-y)
            j = max(x, y, size-x-y)

            if visited[i][j] == False:
                q.append((i, j))
                visited[i][j] = True

    print(0)

rock_group = list(map(int, input().split()))
size = sum(rock_group)

if size % 3 != 0:
    print(0)
else:
    bfs(min(rock_group), max(rock_group))