def findParent(node):
    global k

    return (node + k - 2) // k

n, k, q = map(int, input().split())

for _ in range(q):
    # 부모노드 = (자식 노드 + k - 2) // k
    # 부모노드가 같으면 두 노드 간의 거리를 구할 수 있음
    # 둘 중 큰 노드 먼저 부모 노드 구함 -> 노드 비교
    x, y = map(int, input().split())

    cnt = 0
    
    if k == 1:
        cnt = abs(x - y)
    else:
        while x != y:
            if x > y:
                x = findParent(x)
            else:
                y = findParent(y)

            cnt += 1

    print(cnt)