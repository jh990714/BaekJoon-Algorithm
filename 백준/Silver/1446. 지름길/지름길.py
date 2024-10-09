import sys

input = sys.stdin.readline

n, d = map(int, input().split())

load = []
for _ in range(n):
    start, end, len = map(int, input().split())
    if end - start > len:
        load.append((start, end, len))
load.sort()

load_dp = [i for i in range(d+1)]

for start, end, len in load:
    for i in range(start, d+1):
        if end == i:
            load_dp[i] = min(load_dp[i], load_dp[start] + len)
        else:
            load_dp[i] = min(load_dp[i], load_dp[i-1] + 1)

print(load_dp[d])