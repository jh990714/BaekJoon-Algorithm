import sys

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
bytes = [*map(int, input().split())]
costs = [*map(int, input().split())]

sum_costs = sum(costs)
dp = [[0] * (sum_costs+1) for _ in range(N)]

min_cost = INF
for i in range(N):
    byte = bytes[i]
    cost = costs[i]

    for j in range(sum_costs + 1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost] + byte)

        # min_cost이상은 필요 x
        if min_cost < j or dp[i][j] >= M:
            min_cost = min(min_cost, j)
            break

print(min_cost)