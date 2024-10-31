scret = input()

dp = [0] * (len(scret)+1)

dp[0] = 1
dp[1] = 1

if scret[0] == '0':
    print(0)

else:
    for i in range(1, len(scret)):
        if scret[i] > '0':
            dp[i+1] += dp[i]

        if '10' <= scret[i-1] + scret[i] <= '26':
            dp[i+1] += dp[i-1]

    print(dp[-1] % 1000000)