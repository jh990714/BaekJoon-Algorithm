import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]
min_cost = INF

for i in range(3):
    dp = [[INF] * 3  for _ in range(N)]
    dp[0][i] = rgb[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + rgb[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + rgb[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + rgb[j][2]

    for j in range(3):
        if i != j:
            min_cost = min(min_cost, dp[-1][j])
    
print(min_cost)