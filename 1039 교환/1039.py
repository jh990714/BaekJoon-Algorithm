import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    q = deque()
    q.append((n, 0))

    visited = []
    visited.append((n, 0))

    k_max = 0
    while q:
        n, cnt = q.popleft()
        if cnt == k:
            k_max = max(k_max, n)
            continue

        for i in range(len_n-1):
            for j in range(i+1, len_n):
                str_n = list(str(n))
                
                if i == 0 and str_n[j] == '0':
                    continue
                
                str_n[i], str_n[j] = str_n[j], str_n[i]
                int_n = int(''.join(str_n))

                if (int_n, cnt+1) not in visited:
                    q.append((int_n, cnt+1))
                    visited.append((int_n, cnt+1))

    return k_max if k_max else -1

N, K = map(int, input().split())
len_n = len(str(N))

print(bfs(N, K))
