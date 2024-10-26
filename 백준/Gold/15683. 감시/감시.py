# 방향 벡터 정의 (하, 우, 상, 좌)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# CCTV 종류별 감시 방향 조합 정의
cctv_directions = [
    [[0], [1], [2], [3]],  # 1번 CCTV
    [[0, 2], [1, 3]],      # 2번 CCTV
    [[0, 1], [1, 2], [2, 3], [0, 3]],  # 3번 CCTV
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [0, 1, 3]],  # 4번 CCTV
    [[0, 1, 2, 3]],        # 5번 CCTV (모든 방향 감시)
]

def watch(x, y, direction, graph):
    """CCTV가 주어진 방향으로 감시하는 함수 (상태 변경)"""
    for d in direction:
        nx, ny = x, y
        while True:
            nx += directions[d][0]
            ny += directions[d][1]
            # 범위를 벗어나거나 벽(6)을 만나면 중단
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 6:
                break
            # 빈 칸(0)만 감시 표시
            if graph[nx][ny] == 0:
                graph[nx][ny] = '#'

def dfs(depth):
    """DFS 탐색과 백트래킹을 사용한 최적화된 CCTV 배치 탐색"""
    global answer

    if depth == len(cctvs):  # 모든 CCTV를 배치한 경우 남은 0의 개수 계산
        count = sum(row.count(0) for row in room)
        answer = min(answer, count)
        return

    # 현재 CCTV의 정보 가져오기
    cctv_type, x, y = cctvs[depth]

    original = [row[:] for row in room]  # 백트래킹을 위해 원본 저장

    # 해당 CCTV의 가능한 모든 방향 조합에 대해 탐색
    for direction in cctv_directions[cctv_type]:
        watch(x, y, direction, room)  # 감시 실행
        dfs(depth + 1)  # 다음 CCTV 배치
        room[:] = [row[:] for row in original]  # 백트래킹 (원본 복구)

# 입력 처리
n, m = map(int, input().split())
room = []
cctvs = []

for i in range(n):
    row = list(map(int, input().split()))
    room.append(row)
    for j in range(m):
        if 1 <= row[j] <= 5:  # CCTV 발견 시 리스트에 추가
            cctvs.append((row[j] - 1, i, j))

answer = float('inf')  # 최소 사각지대 크기 초기화
dfs(0)  # DFS 탐색 시작
print(answer)  # 결과 출력
