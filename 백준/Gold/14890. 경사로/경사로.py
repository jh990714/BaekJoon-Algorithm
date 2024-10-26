n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def check(road):
    visited = [False] * len(road)  # 경사로가 놓였는지 체크하는 리스트

    for i in range(len(road) - 1):
        # 1. 높이 차이가 2 이상이면 경사로 불가
        if abs(road[i] - road[i + 1]) > 1:
            return False
        
        # 2. 내려가는 경사로 체크 (road[i] > road[i + 1])
        if road[i] - road[i + 1] == 1:
            for j in range(i + 1, i + 1 + l):
                if j >= len(road) or road[j] != road[i + 1] or visited[j]:
                    return False
                visited[j] = True  # 경사로 설치
            
        # 3. 올라가는 경사로 체크 (road[i] < road[i + 1])
        elif road[i + 1] - road[i] == 1:
            for j in range(i, i - l, -1):
                if j < 0 or road[j] != road[i] or visited[j]:
                    return False
                visited[j] = True  # 경사로 설치

    return True

cnt = 0

# 1. 행 검사
for row in board:
    if check(row):
        cnt += 1

# 2. 열 검사
for col in range(n):
    column = [board[row][col] for row in range(n)]
    if check(column):
        cnt += 1

print(cnt)
