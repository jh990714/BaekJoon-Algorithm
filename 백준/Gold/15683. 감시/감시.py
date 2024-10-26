import copy

dirctions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cctv_directions =  [
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

def dfs(idx, tlst):
    global answer

    if idx == len(cctvs):
        answer = min(answer, zero_cnt(tlst))
        return


    level, x, y = cctvs[idx]

    for cctv_direction in cctv_directions[level]:
        dfs(idx+1, tlst + [cctv_direction])

        
def zero_cnt(tlst):
    room_copy = copy.deepcopy(room)

    for cctv, cctv_direction in zip(cctvs, tlst):
        

        for d in cctv_direction:
            # print(tlst, d, dirctions[d])
            _, nx, ny = cctv
            dx, dy = dirctions[d]

            while True:
                nx += dx
                ny += dy

                if not (0 <= nx < n and 0 <= ny < m):
                    break

                if room_copy[nx][ny] == 6:
                    break

                room_copy[nx][ny] = '#'
        
            # for i in room_copy:
            #     print(i)
            # print()

    cnt = 0
    for i in range(n):
        cnt += room_copy[i].count(0)

    return cnt

n, m = map(int, input().split())

room = []
cctvs = []
answer = float('inf')

for i in range(n):
    row = list(map(int, input().split()))
    room.append(row)

    for j in range(len(row)):
        if 1 <= row[j] <= 5:
            cctvs.append((row[j]-1, i, j))


dfs(0, [])
print(answer)