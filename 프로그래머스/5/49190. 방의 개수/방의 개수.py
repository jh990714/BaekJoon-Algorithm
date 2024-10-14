from collections import defaultdict

def solution(arrows):
    directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    
    answer = 0
    x, y = 0, 0
    path = defaultdict(list)

    
    for arrow in arrows:
        for _ in range(2):
            dx, dy = directions[arrow]
            nx, ny = x + dx, y + dy

            if (nx, ny) in path and (x, y) not in path[(nx, ny)]:
                answer += 1
            
            path[(x, y)].append((nx, ny))
            path[(nx, ny)].append((x, y))
            
            x, y = nx, ny

    return answer