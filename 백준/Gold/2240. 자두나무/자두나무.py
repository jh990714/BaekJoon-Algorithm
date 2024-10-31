T, W = map(int, input().split())

dp = [[0] * (W+2) for _ in range(T+1)]

for i in range(1, T+1):
    tree = int(input())

    for j in range(1, W+2):
        cur_tree = 1 if j % 2 == 1 else 2

        add_cnt = tree == cur_tree

        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + add_cnt

print(max(dp[-1]))