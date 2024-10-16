import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int, input().split())
edge = []
for _ in range(e):
    edge.append(tuple(map(int, input().split())))

edge.sort(key=lambda x: x[2])

parent = [i for i in range(v+1)]
total_cost = 0
for n1, n2, cost in edge:
    parent_n1 = find_parent(parent, n1)
    parent_n2 = find_parent(parent, n2)

    if parent_n1 != parent_n2:
        union_parent(parent, parent_n1, parent_n2)
        total_cost += cost

print(total_cost)
