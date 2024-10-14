from collections import deque
from collections import defaultdict
 

def solution(game_board, table):
    row, column = len(game_board), len(game_board[0])
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def findPiece(board, target):
        visited = [[False] * column for _ in range(row)]
        number = 1
        pieces = defaultdict(list)
        
        for i in range(row):
            for j in range(column):
                if board[i][j] == target and not visited[i][j]:
                    pieces[number] = bfs((i, j), board, visited, target)
                    number += 1
                    
        return pieces

    def bfs(start, board, visited, target):
        que = deque([start])
        visited[start[0]][start[1]] = True
        path = [(start)]

        min_x, min_y = start

        while que:
            x, y = que.popleft()
            
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                                    
                if not (0 <= nx < row and 0 <= ny < column):
                    continue
                
                if board[nx][ny] != target:
                    continue
                    
                if visited[nx][ny]:
                    continue
                
                visited[nx][ny] = True
                que.append((nx, ny))
                path.append((nx, ny))

        path = [(x - min_x, y - min_y) for x, y in path]
        
        return path

    def rotate(piece):
        # 90도 회전: (x, y) -> (y, -x)
        rotated = [(y, -x) for x, y in piece]

        # 최소 x, y를 찾아 (0, 0) 기준으로 정규화
        min_x = min(x for x, y in rotated)
        min_y = min(y for x, y in rotated)

        normalized = [(x - min_x, y - min_y) for x, y in rotated]

        return normalized
    
    def match(blank, piece):
        return sorted(blank) == sorted(piece)
    
    blank_pieces = findPiece(game_board, 0)
    pieces = findPiece(table, 1)
    
    cnt = 0
    for i, blank in blank_pieces.items():
        for key, piece in list(pieces.items()):
            check = False
            for _ in range(4):
                piece = rotate(piece)
                
                if match(blank, piece):
                    cnt += len(blank)
                    del pieces[key]
                    
                    check = True
                    break
            
            if check:
                break

    return cnt