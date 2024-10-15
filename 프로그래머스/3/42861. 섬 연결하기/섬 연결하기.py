# 최단경로 찾기

def solution(n, costs):
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        
        return parent[x]
    
    def union_parent(parent, a, b):
        if a > b:
            parent[b] = a
        else:
            parent[a] = b
    
    answer = 0
    costs.sort(key = lambda x: x[2])
    parent = [i for i in range(n)]
    
    for u, v, cost in costs:
        parent_u = find_parent(parent, u)
        parent_v = find_parent(parent, v)
        if parent_u != parent_v:
            union_parent(parent, parent_u, parent_v)
            answer += cost
        
    return answer