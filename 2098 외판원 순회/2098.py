import sys

input = sys.stdin.readline
INF = sys.maxsize

def dfs(v, visited):
    # 모든 노드 방문
    if visited == (1 << N) - 1:
        if graph[v][0] != 0:
            return graph[v][0]
        else:
            return INF

    # 이미 방문한 노드
    if (v, visited) in dp:
        return dp[(v, visited)]
    
    min_cost = INF
    for nv in range(N):
        if graph[v][nv] == 0 or visited & (1 << nv):
            continue

        min_cost = min(min_cost, dfs(nv, visited | (1 << nv)) + graph[v][nv])
    
    dp[(v, visited)] = min_cost
    return min_cost
    
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = {}

print(dfs(0, 1))