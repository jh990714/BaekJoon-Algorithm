import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    
    return parent[x]

def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

def point_dist(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

n = int(input())
stars = []
for _ in range(n):
    stars.append(tuple(map(float, input().split())))

dists = []
for i in range(n - 1):
    for j in range(i+1, n):
        dist = point_dist(stars[i], stars[j])
        dists.append((dist, i, j))

dists.sort()
        
parent = [i for i in range(n)]
total_dist = 0
for dist, n1, n2 in dists:
    parent_n1 = find_parent(parent, n1)
    parent_n2 = find_parent(parent, n2)

    if parent_n1 != parent_n2:
        union_parent(parent, parent_n1, parent_n2)
        total_dist += dist

print(round(total_dist, 2))
