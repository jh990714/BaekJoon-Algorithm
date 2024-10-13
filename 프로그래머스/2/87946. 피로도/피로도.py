answer = 0

def dfs(k, cnt, visited, dungeons):
    global answer
    
    if cnt > answer:
        answer = cnt
        
    for i in range(len(dungeons)):
        need_energy = dungeons[i][0]
        use_energy = dungeons[i][1]
        
        if not visited[i] and k >= need_energy:
            visited[i] = True
            dfs(k-use_energy, cnt+1, visited, dungeons)
            visited[i] = False
            
def solution(k, dungeons):
    visited = [False] * k
    dfs(k, 0, visited, dungeons)
    
    return answer
    