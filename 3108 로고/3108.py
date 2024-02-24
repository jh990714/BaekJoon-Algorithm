import sys

input = sys.stdin.readline

def connect_rects_line(rect1, rect2):
    if (rect1[1][0] < rect2[0][0] or rect2[1][0] < rect1[0][0] or
        rect1[0][1] > rect2[1][1] or rect2[0][1] > rect1[1][1]):  # 만나지 않을 때
        return False
    
    elif ((rect1[0][0] < rect2[0][0] < rect2[1][0] < rect1[1][0] and
          rect1[0][1] < rect2[0][1] < rect2[1][1] < rect1[1][1]) or
          (rect2[0][0] < rect1[0][0] < rect1[1][0] < rect2[1][0] and
          rect2[0][1] < rect1[0][1] < rect1[1][1] < rect2[1][1])): # 안에 들어가 있을 때
        return False
    
    return True

def find_root(i):
    if group[i] != i:
        group[i] = find_root(group[i])

    return group[i]

N = int(input())
rects = []
point_check = 0
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rects.append(((x1, y1), (x2, y2)))

    if ((x1*x2 == 0) and y1 <= 0 <= y2) or ((y1*y2 == 0) and x1 <= 0 <= x2):
        point_check = 1
        
group = list(range(N))
for i in range(N-1):
    for j in range(i+1, N):
        if connect_rects_line(rects[i], rects[j]):
            root1 = find_root(i)
            root2 = find_root(j)
            group[root1] = root2
            
for i in range(N):
    find_root(i)

print(len(set(group)) - point_check)