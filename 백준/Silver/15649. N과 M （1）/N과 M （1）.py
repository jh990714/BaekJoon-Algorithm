from collections import deque

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solution(n, m):
    visited = [False] * (n+1)
    result = []

    def dfs(depth):
        if depth == m:
            print(' '.join(map(str, result)))
            return
        
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                result.append(i)

                dfs(depth + 1)

                result.pop()
                visited[i] = False
                
    dfs(0)

if __name__ == "__main__":
    n, m = map(int, input().split())

    solution(n, m)