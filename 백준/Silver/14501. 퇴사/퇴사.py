n = int(input())

dp = [0] * (n+1)
for i in range(n):
    t, p = map(int, input().split())
    
    dp[i + 1] = max(dp[i + 1], dp[i])

    j = i + t
    if j <= n:
        dp[j] = max(dp[j], dp[i] + p)

print(dp[-1])