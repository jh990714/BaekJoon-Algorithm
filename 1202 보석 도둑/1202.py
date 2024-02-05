import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()

tmp_jewels = []
result = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        m, v = heapq.heappop(jewels)
        heapq.heappush(tmp_jewels, -v)

    if tmp_jewels:
        result -= heapq.heappop(tmp_jewels)

print(result)