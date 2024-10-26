from collections import deque

RIGHT = 1
LEFT = -1

def rotate(wheel, direction):
    if direction == RIGHT: # 시계방향
        wheel.appendleft(wheel.pop())

    elif direction == LEFT: # 반시계방향
        wheel.append(wheel.popleft())

def dfs(n, visited, direction):
    visited.add(n)

    if n-1 >= 0 and n-1 not in visited:
        if cogwheels[n][6] != cogwheels[n - 1][2]:
            dfs(n-1, visited, -direction)

    if n+1 < 4 and n+1 not in visited:
        if cogwheels[n][2] != cogwheels[n + 1][6]:
            dfs(n+1, visited, -direction)
    
    rotate(cogwheels[n], direction)

def calculate_score():
    score = 0
    for i, wheel in enumerate(cogwheels):
        if wheel[0] == '1':
            score += 2**i 
    return score

cogwheels = [deque(list(input())) for _ in range(4)]

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())

    dfs(n-1, set(), d)

print(calculate_score())