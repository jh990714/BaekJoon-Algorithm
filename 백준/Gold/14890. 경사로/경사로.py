n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(road, visited):
    stack = []

    idx = 0
    while idx != len(road):
        if not stack:
            stack.append(road[idx])
    
        else:
            if road[idx] == stack[-1]:
                stack.append(road[idx])

            elif stack[-1] - road[idx] == 1:
                stack = []
                stack.append(road[idx])

            elif road[idx] - stack[-1] == 1:
                if len(stack) >= l:
                    for i in range(l):
                        if visited[idx-i-1]:
                            return False

                        visited[idx-i-1] = True

                    stack = []
                    stack.append(road[idx])
                else:
                    return False
            else:
                return False

        idx += 1

    return True

cnt = 0
for row in board:
    visited = [False] * n
    if check(row, visited) and check(row[::-1], visited[::-1]):
        cnt += 1

for col in range(len(board[0])):
    column = [row[col] for row in board]
    visited = [False] * n
    if check(column, visited) and check(column[::-1], visited[::-1]):
        cnt += 1

print(cnt)
"""
스택에 저장

list[-1] == 높이 -> 스택에 저장
list[-1] - 높이 == 1 -> 스택 비우고 높이 append
높이 - list[-1] == 1 -> 스택 길이가 l 이상이면 지나갈 수 있음, 스택 비우고 높이 append

"""