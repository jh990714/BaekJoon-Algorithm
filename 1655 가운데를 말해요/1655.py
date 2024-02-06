import sys
import heapq

input = sys.stdin.readline

max_heapq = []
min_heapq = []

N = int(input())
for _ in range(N):
    num = int(input())

    if len(min_heapq) > len(max_heapq):
        heapq.heappush(max_heapq, num)
    else:
        heapq.heappush(min_heapq, -num)

    if max_heapq and min_heapq:
        if max_heapq[0] < -min_heapq[0]:
            max_heapq_top = heapq.heappop(max_heapq)
            min_heapq_top = heapq.heappop(min_heapq)

            heapq.heappush(max_heapq, -min_heapq_top)
            heapq.heappush(min_heapq, -max_heapq_top)
    
    print(-min_heapq[0])