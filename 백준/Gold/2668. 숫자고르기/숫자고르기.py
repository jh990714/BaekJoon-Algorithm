import sys

input = sys.stdin.readline

def dfs(n):
    if visited[n]:
        answer.add(n)
        return
    
    visited[n] = True
    dfs(matrix[n])


n = int(input())
matrix = [0]
for _ in range(1, n+1):
    matrix.append(int(input()))

answer = set()
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i)

print(len(answer))
print(*sorted(answer), sep='\n')