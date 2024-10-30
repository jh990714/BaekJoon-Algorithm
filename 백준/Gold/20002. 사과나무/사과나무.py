n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + board[i-1][j-1]

answer = float('-inf')
for k in range(1, n + 1):
    for i in range(k, n + 1):
        for j in range(k, n + 1):
            result = dp[i][j] - dp[i][j-k] - dp[i-k][j] + dp[i-k][j-k]

            answer = max(answer, result)

print(answer)